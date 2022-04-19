import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

const COLOR_BLACK = Color.fromARGB(255, 25, 26, 25);
const COLOR_DARK_GREEN = Color.fromARGB(255, 30, 81, 40);
const COLOR_LIGHT_GREEN = Color.fromARGB(255, 77, 159, 61);
const COLOR_YELLOW_GREEN = Color.fromARGB(255, 216, 233, 168);
const COLOR_WHITE = Color.fromARGB(255, 255, 255, 255);

TextTheme defaultText = TextTheme(
    headline1: GoogleFonts.nunito(fontWeight: FontWeight.bold, fontSize: 96),
    headline2: GoogleFonts.nunito(fontWeight: FontWeight.bold, fontSize: 60),
    headline3: GoogleFonts.nunito(fontWeight: FontWeight.bold, fontSize: 48),
    headline4: GoogleFonts.nunito(fontWeight: FontWeight.bold, fontSize: 34),
    headline5: GoogleFonts.nunito(fontWeight: FontWeight.bold, fontSize: 24),
    headline6: GoogleFonts.nunito(fontWeight: FontWeight.bold, fontSize: 20),
    bodyText1: GoogleFonts.nunito(fontSize: 16, fontWeight: FontWeight.normal),
    bodyText2: GoogleFonts.nunito(
      fontSize: 14,
      fontWeight: FontWeight.normal,
    ),
    subtitle1: GoogleFonts.nunito(fontSize: 16, fontWeight: FontWeight.normal),
    subtitle2: GoogleFonts.nunito(fontSize: 14, fontWeight: FontWeight.w400),
    button: GoogleFonts.nunito(fontSize: 14, fontWeight: FontWeight.w400),
    caption: GoogleFonts.nunito(fontSize: 12, fontWeight: FontWeight.normal));
