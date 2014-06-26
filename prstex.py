"""
An IPython extension for generating LaTeX sniplets and adding them to your
ipython notebook 
"""
import os
from IPython.core.magic import magics_class, cell_magic, Magics
from IPython.display import Image, SVG

latex_template_chp = r"""\documentclass{article}
\usepackage[%s]{prs}
\begin{document}
\thispagestyle{empty}

\begin{csp}
%s
\end{csp} 


\end{document}
"""

latex_template_prs = r"""\documentclass{article}
\usepackage[%s]{prs}
\begin{document}
\thispagestyle{empty}

\begin{prs}
%s
\end{prs} 


\end{document}
"""

@magics_class
class prstex(Magics):

    @cell_magic
    def prstex(self, line, cell):
        """Generate and display a prs diagram using LaTeX/prslatex
        
        Usage:
        
            %prstex [key1=value1] [key2=value2] ...

            Possible keys and default values are

                filename = ipynb-circuitikz-output
                options =  options to the pdflatexpackage
        """
        options = {'filename': 'ipynb-circuitikz-output', 'options':''}
                   


        for option in line.split(" "):
            try:
                key, value = option.split("=")
                if key in options:
                    options[key] = value
                else:
                    print("Unrecongized option %s" % key)
            except:
                pass

        filename = options['filename']
        code = cell

        os.system("rm -f %s.tex %s.pdf %s.png" % (filename, filename, filename))        

        with open(filename + ".tex", "w") as file:
            file.write(latex_template_prs % (options['options'], cell))
    
        os.system("pdflatex -interaction batchmode %s.tex" % filename)
        os.system("rm -f %s.aux %s.log" % (filename, filename))        
        os.system("pdfcrop %s.pdf %s-tmp.pdf" % (filename, filename))
        os.system("mv %s-tmp.pdf %s.pdf" % (filename, filename))        

        os.system("pdf2svg %s.pdf %s.svg" % (filename, filename))
        result = SVG(filename + ".svg")

        return result

@magics_class
class chptex(Magics):

    @cell_magic
    def chptex(self, line, cell):
        """Generate and display a chp using LaTeX/prslatex
        
        Usage:
        
            %chptex [key1=value1] [key2=value2] ...

            Possible keys and default values are

                filename = ipynb-circuitikz-output
                options =  options to the pdflatexpackage
        """
        options = {'filename': 'ipynb-circuitikz-output', 'options':''}
                   


        for option in line.split(" "):
            try:
                key, value = option.split("=")
                if key in options:
                    options[key] = value
                else:
                    print("Unrecongized option %s" % key)
            except:
                pass

        filename = options['filename']
        code = cell

        os.system("rm -f %s.tex %s.pdf %s.png" % (filename, filename, filename))        

        with open(filename + ".tex", "w") as file:
            file.write(latex_template_chp % (options['options'], cell))
    
        os.system("pdflatex -interaction batchmode %s.tex" % filename)
        os.system("rm -f %s.aux %s.log" % (filename, filename))        
        os.system("pdfcrop %s.pdf %s-tmp.pdf" % (filename, filename))
        os.system("mv %s-tmp.pdf %s.pdf" % (filename, filename))        

        os.system("pdf2svg %s.pdf %s.svg" % (filename, filename))
        result = SVG(filename + ".svg")

        return result


def load_ipython_extension(ipython):
    ipython.register_magics(prstex)
    ipython.register_magics(chptex)

