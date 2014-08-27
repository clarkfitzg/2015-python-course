paper.pdf : paper.tex figure.pdf make_graph.pdf plot.R Makefile
	pdflatex paper.tex

# Running vanilla means that R won't save or use .RData files
figure.pdf : data.csv plot.R
	R CMD BATCH --vanilla plot.R

data.csv : get_data.py
	python get_data.py

make_graph.pdf : make_graph.dot
	dot -Tpdf make_graph.dot -o make_graph.pdf

make_graph.dot : make_graph.py Makefile
	python make_graph.py > make_graph.dot

clean :
	rm *.Rout *.aux *.log *.out
