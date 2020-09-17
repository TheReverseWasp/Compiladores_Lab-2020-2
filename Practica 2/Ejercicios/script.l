  int contador = 1;
  char inicio[] = "\\begin{tabular}{|c|p{3cm}|p{8cm}|p{2cm}|} \\hline \n";
  char fin[] = "\\hline\n\\end{tabular}";

  int main(){
    yylex();
    printf("Se conto %d lineas", contador);
  }

%%
hora  {(1[0-2]:[0-5][0-9] ([(a. m.)|(p. m.)]))}
true_hora (\[{hora})
dia   {[1-9]|([1-2][0-9])|(3[0-1])}
mes   {[1-9]|(1[0-2])}
anio  {[1-9][1-9][1-9][1-9]}
true_fecha  ({dia}/{mes}/{anio}\])
nombre  {[a-z|A-Z|0-9| ]+}
var_name  {\] {nombre}:}
simbolos  {[\.|\,|\[|\]|-|_|=]}
mensaje   ([{nombre}|({simbolo}+)])
true_mensaje  ({: {mensaje}$})
%%
{true_hora} { char true_hora[] = ECHO; int t = 0; while(true_hora[t + 1] != '\0') {true_hora[t] = true_hora[t + 1]; t += 1;}; true_hora[t] = '\0';  }
{true_fecha}  { char true_fecha[] = ECHO; int t = 0; while(true_fecha[t + 1] != ']') {t += 1;}; true_fecha[t + 1] = '\0';  }
{var_name} { char var_name = ECHO; int t = 2; while(var_name[t] != ':') {var_name[t-2] = var_name[t];}; var_name[t] = '\0'; var_name[t-1] = '\0'; }
{true_mensaje}  { char true_mensaje = ECHO; int t = 2; while(true_mensaje[t] != ':') {true_mensaje[t-2] = true_mensaje[t];}; true_mensaje[t] = '\0'; true_mensaje[t-1] = '\0'; }
$ { printf("%s", inicio); printf("\t\\textsc{%s}\n\t%d & %s \n\t\\begin{tabular}{c}\n\t\t\\footnotesize{%s} \\\\\n\t\t\\Large{\\textbf{%s}} \\\\\n\t\\end{tabular} \\\n%s", var_name, contador, true_mensaje, true_fecha, true_hora, fin); }
%%
