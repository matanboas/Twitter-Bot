import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

const COLOR_BLACK = Color.fromARGB(255, 25, 26, 25);
const COLOR_DARK_GREEN = Color.fromARGB(255, 30, 81, 40);
const COLOR_LIGHT_GREEN = Color.fromARGB(255, 77, 159, 61);
const COLOR_YELLOW_GREEN = Color.fromARGB(255, 216, 233, 168);
const COLOR_WHITE = Color.fromARGB(255, 255, 255, 255);

TextTheme defaultText = TextTheme(
  headline1: GoogleFonts.montserrat(
      fontWeight: FontWeight.w300, fontSize: 75, color: COLOR_WHITE),
  headline2: GoogleFonts.montserrat(
      fontWeight: FontWeight.w300, fontSize: 75, color: COLOR_BLACK),
  headline3: GoogleFonts.montserrat(
      fontWeight: FontWeight.w600, fontSize: 55, color: COLOR_WHITE),
  headline4: GoogleFonts.montserrat(
      fontWeight: FontWeight.w600, fontSize: 55, color: COLOR_BLACK),
  subtitle1: GoogleFonts.nunito(
      fontSize: 30, fontWeight: FontWeight.w400, color: COLOR_WHITE),
);
