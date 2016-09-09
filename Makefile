
po_files = $(wildcard po/*.po)
mo_files = $(patsubst po/%.po,correcthorse/messages/%/LC_MESSAGES/correcthorse.mo,$(po_files))
runtime_files = $(mo_files)

.PHONY: all
all:	$(runtime_files)

.PHONY: update-translations
update-translations:
	cd po && intltool-update -g correcthorse -p
	for po in $(po_files); do msgmerge -U $$po po/correcthorse.pot; done


correcthorse/messages/%/LC_MESSAGES/correcthorse.mo: po/%.po
	mkdir -p $(@D)
	msgfmt -o $@ $<


.PHONY: clean
clean:
	rm -rf temp dist tmp build correcthorse.egg-info $(runtime_files)
	find -name '*.pyc' -delete
