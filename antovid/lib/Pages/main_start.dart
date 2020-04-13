import 'package:flutter/material.dart';
import 'home_screen.dart';

class StartPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AntoVID',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: BaseHome(),
    );
  }
}
