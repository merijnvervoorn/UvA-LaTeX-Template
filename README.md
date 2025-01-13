# 📄 University of Amsterdam LaTeX Template

This repo holds the LaTeX template I use when writing my reports.

## 🪛 Setup

I use [Overleaf](https://www.overleaf.com/) as my LaTeX editor.
The main.tex file is the main file (No shit, Sherlock). This file references the other .tex files.
For referencing I use the apacite package, this follows APA 6th Edition rules. You can find more about the package via [apacite.pdf](apacite.pdf). Use "A study \cite{lastname2025entry}..." for citations, or "In a study by Lastname \citeyear{lastname2025entry}..." for intext citations.

## 🔨 Customization

You can modify the files to suit your preferences:

- Include your name and email: Of course you should swap out my name and email with yours.
- Change or remove logos: The file includes my personal logo and the logo for my study programme. You should probably change these out for the relevant logos of your course.
- Add appendices: The main.tex file includes the possibility to add an abstract and appendices. The abstract can just be uncommented and then written. The appendices should be created in a new file, you can input the name of this/these file(s) in the main.tex file.

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for more details

## 🔍 Acknowledgments

This script uses various LaTeX tools, such as hyperref, apacite and fancyhdr.
Thanks to all contributors to the Overleaf help guides used in this setup.
