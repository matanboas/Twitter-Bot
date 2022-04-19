import 'package:flutter/material.dart';
import 'constants.dart';

class MyFlatButton extends StatelessWidget {
  const MyFlatButton(
      {Key? key,
      required this.text,
      required this.onPressed,
      required this.color})
      : super(key: key);
  final String text;
  final void Function() onPressed;
  final Color color;

  @override
  Widget build(BuildContext context) {
    final TextTheme textTheme = Theme.of(context).textTheme;

    return Container(
        height: MediaQuery.of(context).size.height * 0.08,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(60),
          color: color,
        ),
        child: Material(
          child: InkWell(
            customBorder: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(60),
            ),
            onTap: () => onPressed(),
            child: Center(
              child: Text(text, style: textTheme.subtitle1),
            ),
          ),
          color: COLOR_WHITE.withOpacity(0.0),
        ));
  }
}
