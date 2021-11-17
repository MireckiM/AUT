
# .far to specjalny format do przechowywania spakowanych transduktorów

BINARIES += TaskC06/C06.far

TaskC06/run: TaskC06/C06.far

TaskC06/C06.far: TaskC06/C06.grm
	LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/lib/fst" thraxcompiler --input_grammar=$< --output_far=$@
