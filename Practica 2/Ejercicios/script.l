line \[[.]*$;
    int contador = 1;
    void fun(char *line) {
      int sz = sizeof(line) / sizeof(line[0]);
      char hora[10];
      char periodo[10];
      char fecha[15];
      char nombre[30];
      char mensaje[200];
      int it = 1, pos = 0;
      printf("%d", sz);
      while(line[it] != ' ' && it < sz) {
        hora[pos] = line[it];
        it++;
        pos++;
      }
      it++;
      pos = 0;
      while(line[it] != ',' && it < sz) {
        periodo[pos] = line[it];
        it++;
        pos++;
      }
      it += 2;
      pos = 0;
      while(line[it] != ']' && it < sz) {
        fecha[pos] = line[it];
        it++;
        pos++;
      }
      pos = 0;
      it += 2;
      while(line[it] != ':' && it < sz) {
        nombre[pos] = line[it];
        pos++;
        it++;
      }
      pos = 0;
      it += 2;
      while(it < sz) {
        mensaje[pos] = line[it];
        pos++;
        it++;
      }
      printf("\\begin{tabular}{|c|p{3cm}|p{8cm}|p{2cm}|} \\hline\n\t\\textsc{%s} &\n", nombre);
      printf("\t%d\n", contador);
      printf("\t%s &\n", mensaje);
      printf("\t\\begin{tabular}{c}\n\t\t\\footnotesize{%s} \\\\\n", fecha);
      printf("\t\t\\Large{\\textbf{%s}} \\\\\n", hora);
      printf("\t\t%s\n\t\\end{tabular} \\\\\n", periodo);
      printf("\\hline\n\\end{tabular}\n");
      contador++;
    }
%%
{line}  { fun(yytext);  }
%%

int main()
{
  yylex();
}
