import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:charts_flutter/flutter.dart' as charts;
import 'package:flutter/material.dart';
import 'notification_start.dart';
import 'state_view.dart';

List<String> country=List();
class BaseHome extends StatelessWidget {
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
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: TopScreen(),
            ),
            flex: 1,
          ),
          Divider(),
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: BottomScreen(),
            ),
            flex: 1,
          ),
        ],
      ),
    );
  }
}

class BottomScreen extends StatelessWidget {
  const BottomScreen({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return StreamBuilder(
        stream: Firestore.instance
            .collection('Country')
            .document('World')
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
  const TopScreen({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return StreamBuilder(
        stream: Firestore.instance
            .collection('Country')
            .snapshots(),
        builder: (context, snapshot) {
          if (snapshot.hasData)
            return ListView.builder(
                itemCount: snapshot.data.documents.length,
                itemBuilder: (context, index) {
                  country.add(snapshot.data.documents[index].documentID.toString());
                  return ListTile(
                    onTap: () => snapshot.data.documents[index].documentID.toString()=='India'?Navigator.push(context, MaterialPageRoute(builder: (context)=>StateView(countryName:snapshot.data.documents[index].documentID.toString(),country: country,))):null,
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
