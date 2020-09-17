.SUFFIXES:
.SUFFIXES: .svg  




a_svg = $(patsubst %.svg,%.pdf,$(wildcard *.svg))

dirs = Modulaciones_digitales/lab17/svg \
       Modulaciones_digitales/lab18/svg \
       Modulaciones_digitales/lab19/svg \
       Modulaciones_digitales/lab20/svg \
       Modulaciones_digitales/lab21/svg \
       Modulaciones_digitales/lab22/svg \
       Modulaciones_digitales/lab23/svg \
       Modulaciones_digitales/lab24/svg \
       Modulaciones_digitales/lab25/svg 

#dirs = parte3/lab8/svg 
.PHONY: 

.PHONY: todo $(dirs) clean

todo:  $(dirs) $(a_svg) libro

libro:
	latexmk -pdf SDR-digital.tex


$(dirs):
	$(MAKE) -C $@



clean:
	for dir in $(dirs); do \
	$(MAKE) -C $$dir -f Makefile $@; \
	done
	latexmk -c
