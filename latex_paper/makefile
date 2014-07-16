paper.pdf : paper.tex figure.pdf
	pdflatex paper.tex

# Running R with vanilla means that it won't save or use .RData files
figure.pdf : data.csv plot.R
	R CMD BATCH --vanilla plot.R

data.csv : get_data.py
	python get_data.py
