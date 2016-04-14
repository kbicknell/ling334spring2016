codebase=python_part3
codehtml=$(addsuffix .html, $(codebase))
codemd=$(addsuffix .md, $(codebase))
all : $(codehtml)

.PHONY : all clean

%.html : %.md
	Rscript -e "require(rmarkdown); render('$<')"

%.md : %.Pnw
	Pweave -f pandoc $^

clean :
	rm -f $(codehtml)
	rm -f $(codemd)
