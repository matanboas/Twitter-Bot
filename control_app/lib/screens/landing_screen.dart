import 'package:control_app/utils/widget_functions.dart';
import 'package:flutter/material.dart';
import '../utils/constants.dart';
import '../utils/button.dart';

class LandingScreen extends StatelessWidget {
  const LandingScreen({Key? key}) : super(key: key);

  void printOk() {
    print('ok');
  }

  @override
  Widget build(BuildContext context) {
    final TextTheme textTheme = Theme.of(context).textTheme;

    return Scaffold(
      body: Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        decoration: const BoxDecoration(
          image: DecorationImage(
            image: AssetImage('assets/images/background.png'),
            fit: BoxFit.fill,
          ),
        ),
        child: Padding(
          padding: const EdgeInsets.symmetric(
            vertical: 70.0,
            horizontal: 40.0,
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text("Hello,", style: textTheme.headline1),
                  Text("Matan", style: textTheme.headline3),
                ],
              ),
              Column(
                children: [
                  Center(
                    child: MyFlatButton(
                        text: 'Start Tweeting!',
                        onPressed: () => printOk(),
                        color: COLOR_LIGHT_GREEN),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
