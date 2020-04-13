import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:charts_flutter/flutter.dart' as charts;
import 'package:flutter/material.dart';
import 'notification_start.dart';
import 'district_view.dart';

//var defaultState;
class StateView extends StatefulWidget {
  final String countryName;
  final List<String> country;
  StateView({this.country, this.countryName});

  @override
  _StateViewState createState() => _StateViewState();
}

class _StateViewState extends State<StateView> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: [
          IconButton(
              icon: Icon(Icons.settings),
              onPressed: () => Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => NotificationStartPage())))
        ],
      ),
      body: Column(
        children: <Widget>[
          /* 
Padding(
              padding: const EdgeInsets.all(8.0),
              child: Card(
                child: Container(
                  child: DropdownButton<String>(
                    value: defaultState,
                    items: widget.country.map((String value) {
                      return DropdownMenuItem<String>(
                        value: value,
                        child: Text(value),
                      );
                    }).toList(),
                    onChanged: (value) {
                      setState(() {
                        defaultState = value;
                      });
                    },
                  ),
                ),
              ),
            ), */
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: TopScreen(
                countryName: widget.countryName,
              ),
            ),
            flex: 1,
          ),
          Divider(),
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: BottomScreen(
                countryName: widget.countryName,
              ),
            ),
            flex: 1,
          ),
        ],
      ),
    );
  }
}

class BottomScreen extends StatelessWidget {
  final countryName;
  const BottomScreen({
    this.countryName,
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return StreamBuilder(
        stream: Firestore.instance
            .collection('Country')
            .document(countryName.toString())
            .snapshots(),
        builder: (context, snapshot) {
          if (snapshot.hasData)
            return SimpleBarChart(document: snapshot.data);
          else
            return CircularProgressIndicator();
        });
  }
}

class TopScreen extends StatelessWidget {
  final countryName;
  const TopScreen({
    this.countryName,
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return StreamBuilder(
        stream: Firestore.instance
            .collection('Country')
            .document(countryName)
            .collection('States')
            .snapshots(),
        builder: (context, snapshot) {
          if (snapshot.hasData)
            return ListView.builder(
                itemCount: snapshot.data.documents.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    onTap: ()=>Navigator.push(context, MaterialPageRoute(builder: (context)=>DistrictView(stateName: snapshot.data.documents[index].documentID.toString(),countryName: countryName,))),
                    title: Text(
                      snapshot.data.documents[index].documentID.toString(),
                      style: TextStyle(fontSize: 20.0),
                    ),
                    subtitle: Row(
                      children: [
                        Text(
                          "Active: ${snapshot.data.documents[index]['active']}",
                          style: TextStyle(color: Colors.red),
                        ),
                        VerticalDivider(),
                        Text(
                          "Cured: ${snapshot.data.documents[index]['recovered']}",
                          style: TextStyle(color: Colors.green),
                        ),
                        VerticalDivider(),
                        Text(
                          "Effected: ${snapshot.data.documents[index]['cases']}",
                          style: TextStyle(color: Colors.blue),
                        ),
                        VerticalDivider(),
                        Text(
                          "Deceased: ${snapshot.data.documents[index]['deaths']}",
                          style: TextStyle(color: Colors.deepOrange),
                        ),
                      ],
                    ),
                  );
                });
          else
            return Center(child: Text("Please wait..."));
        });
  }
}

class SimpleBarChart extends StatelessWidget {
  final document;
  final List<charts.Series> seriesList; // = _createSampleData();
  final bool animate;

  SimpleBarChart({this.document, this.seriesList, this.animate});

  factory SimpleBarChart.withSampleData() {
    return SimpleBarChart(
      animate: false,
    );
  }

  @override
  Widget build(BuildContext context) {
    return new charts.BarChart(
      _createSampleData(document['active'], document['recovered'],
          document['cases'], document['deaths']),
      animate: animate,
    );
  }

  static List<charts.Series<BarChartUnit, String>> _createSampleData(
      a, c, e, d) {
    final data = [
      new BarChartUnit('Active', a),
      new BarChartUnit('Cured', c),
      new BarChartUnit('Effected', e),
      new BarChartUnit('Deceased', d),
    ];

    return [
      new charts.Series<BarChartUnit, String>(
        id: 'Covid19 Stats',
        colorFn: (_, i) => barColorPallete[i],
        domainFn: (BarChartUnit unit, _) => unit.title,
        measureFn: (BarChartUnit unit, _) => unit.value,
        data: data,
      )
    ];
  }
}

List barColorPallete = [
  charts.MaterialPalette.red.shadeDefault,
  charts.MaterialPalette.green.shadeDefault,
  charts.MaterialPalette.blue.shadeDefault,
  charts.MaterialPalette.deepOrange.shadeDefault
];

class BarChartUnit {
  final String title;
  final int value;

  BarChartUnit(this.title, this.value);
}
