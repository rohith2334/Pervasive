import 'package:flutter/material.dart';
import 'Pages/main_start.dart';
import 'Services/notification_service.dart';

void main() {
  notificationServiceInitiater();
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return StartPage();
  }
}
