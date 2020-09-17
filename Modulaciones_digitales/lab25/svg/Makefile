.SUFFIXES:
.SUFFIXES: .svg  
.SUFFIXES: .png  

asvg = $(patsubst %.svg,../pdf/%.pdf,$(wildcard *.svg))
apng = $(patsubst %.png,../pdf/%.pdf,$(wildcard *.png))


.PHONY: clean

todo: $(asvg) $(apng)


../pdf/%.pdf: %.svg
	@echo ---- Generando el $@ con $< ...
	inkscape -D -A $@ $<
	#mv $@ ../pdf

../pdf/%.pdf: %.png
	@echo ---- Generando el $@ con $< ...
	inkscape -D -A $@ $<
	#mv $@ ../pdf

clean:
	@echo  Borrando: $(asvg)
	- rm -rf $(asvg) 

clean:
	@echo  Borrando: $(apng)
	- rm -rf $(apng) $(asvg)

