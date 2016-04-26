hwbase=hw1 hw2 #hw3 project hw4
hwhtml=$(addsuffix .html, $(hwbase))
all : $(hwhtml)

.PHONY : all clean

%.html : %.Rmd
	Rscript -e "require(rmarkdown); render('$<')"
hw3.html : hw3.Rmd hmm.svg lattice.svg
	Rscript -e "require(rmarkdown); render('$<')"
%.svg : %.pdf
	pdf2svg $^ $@
%.pdf : %.tex
	pdflatex $^

clean :
	rm -f $(hwhtml)
	rm -f hmm.pdf hmm.svg hmm.log hmm.aux
	rm -f lattice.pdf lattice.svg lattice.log lattice.aux
