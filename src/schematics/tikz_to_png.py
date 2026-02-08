import subprocess
import os
import sys

def compile_tikz_to_png(tikz_code, output_filename):
    # Create a standalone LaTeX document with the provided TikZ code
    latex_document = f"""
    \\documentclass{{standalone}}
    \\usepackage{{tikz}}
    \\usetikzlibrary{{
        angles,
        arrows,
        arrows.meta,
        automata,
        calc,
        decorations.pathreplacing,
        fit,
        positioning,
        quotes,
        shapes,
        shapes.multipart,
    }}
    \\input{{../src/schematics/tikzstyles}}

    \\begin{{document}}

    {tikz_code}

    \\end{{document}}
    """

    # Write the LaTeX document to a file
    latex_filename = 'tikz_picture.tex'
    with open(latex_filename, 'w') as file:
        file.write(latex_document)

    # Compile the LaTeX document to PDF using pdflatex
    subprocess.run(['pdflatex', '--shell-escape', latex_filename], check=True)

    # Convert the PDF to SVG using pdf2svg
    pdf_filename = 'tikz_picture.pdf'
    svg_filename = 'tikz_picture.svg'
    subprocess.run(['pdf2svg', pdf_filename, svg_filename], check=True)

    # Convert the SVG to PNG using Inkscape
    png_filename = output_filename
    subprocess.run(['inkscape', svg_filename, '--export-type=png', '--export-filename', png_filename], check=True)

    # Clean up intermediate files
    os.remove(latex_filename)
    os.remove(pdf_filename)
    os.remove(svg_filename)
    os.remove('tikz_picture.log')
    os.remove('tikz_picture.aux')

    print(f"Output saved to {png_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python tikz_to_png.py <input_tikz_file> <output_png_file>")
        sys.exit(1)

    input_tikz_file = sys.argv[1]
    output_png_file = sys.argv[2]

    with open(input_tikz_file, 'r') as file:
        tikz_code = file.read()

    compile_tikz_to_png(tikz_code, output_png_file)

