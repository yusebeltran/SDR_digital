.SUFFIXES:
.SUFFIXES: .svg  
.SUFFIXES: .png  

asvg = $(patsubst %.svg,../pdf/%.pdf,$(wildcard *.svg))
apng = $(patsubst %.png,../pdf/%.pdf,$(wildcard *.png))


.PHONY: clean

todo: $(asvg) $(apng)


../pdf/%.pdf: %.svg
	@echo ---- Generando el archivo: $@ a partir de: $< ...
	@[ -d ../pdf ] || mkdir -v ../pdf 
	@inkscape -D -A $@ $<

../pdf/%.pdf: %.png
	@echo ---- Generando el archivo: $@ a partir de: $< ...
	@[ -d ../pdf ] || mkdir -v ../pdf 
	@inkscape -D -A $@ $<

clean:
	@echo  Borrando: $(asvg)
	- rm -rf $(asvg) 

clean:
	@echo  Borrando: $(apng)
	- rm -rf $(apng) $(asvg)

