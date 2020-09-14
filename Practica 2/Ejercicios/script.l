    int contador = 1;
    char inicio[] = "\\begin{tabular}{|c|p{3cm}|p{8cm}|p{2cm}|} \\hline \n";
    char fin[] = "\\hline\n\\end{tabular}"
%%
hora  {(1[0-2]:[0-5][0-9] ([(a. m.)|(p. m.)]))}
true_hora \[{hora}
{true_hora} {char true_hora[] = ECHO; int t = 0; while(true_hora[t + 1] != '\0') {true_hora[t] = true_hora[t + 1]; t += 1;}; true_hora[t] = '\0';}

dia   {[1-9]|([1-2][0-9])|(3[0-1])}
mes   {[1-9]|(1[0-2])}
anio  {[1-9][1-9][1-9][1-9]}
true_fecha  {dia}/{mes}/{anio}\]
{true_fecha}  {char true_fecha[] = ECHO; int t = 0; while(true_fecha[t + 1] != ']') {t += 1;}; true_fecha[t + 1] = '\0';}

nombre  {[a-z|A-Z|0-9| ]+}
var_name  {\] {nombre}:}
{var_name} {char var_name = ECHO; int t = 2; while(var_name[t] != ':') {var_name[t-2] = var_name[t];}; var_name[t] = '\0'; var_name[t-1] = '\0';}

simbolos  {[\.|\,|\[|\]|-|_|=]}
mensaje   [{nombre}|({simbolo}+)]
true_mensaje  {: {mensaje}$}
{true_mensaje}  {char true_mensaje = ECHO; int t = 2; while(true_mensaje[t] != ':') {true_mensaje[t-2] = true_mensaje[t];}; true_mensaje[t] = '\0'; true_mensaje[t-1] = '\0';}

$       {printf(inicio); printf("\t\\textsc{"); printf(var_name); printf("}\n\t"); printf(contador); printf(" &\n\t"); printf(fin); contador += 1;}
