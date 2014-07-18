paper.pdf : paper.tex figure.pdf Makefile 
	pdflatex paper.tex

# Running vanilla means that R won't save or use .RData files
figure.pdf : data.csv plot.R
	R CMD BATCH --vanilla plot.R

data.csv : get_data.py
	python get_data.py

digraph.pdf : make_graph.py Makefile
	python make_graph.py > make_graph.dot
	dot -Tpdf make_graph.dot -o make_graph.pdf

clean :
	rm *.Rout *.aux *.log
