/*
 * Typical string similarity measurement
 * @author hermanncain
 */

 /*
 * Calculate the length of LCS of 2 strings
 * The same length with x,y: same
 * Smaller: less similar
 * 
 * @params {string/list} x,y
 * @return {class}
 */

function LCS(x,y) {
    this.x = x;
    this.y = y;
    this.islist = Array.isArray(x)
    this.m = x.length;
    this.n = y.length;
    this.r = [];
    this.d = 0;
    this.c = [];

    this.get_length();
    if (this.islist) this.getAllLCS(this.m,this.n,[]);
    else this.getAllLCS(this.m,this.n,'');
}

/* get length of lcs
 * @params void
 * @return void
 */

LCS.prototype.get_length = function () {
    if (this.m==0 || this.n==0) return;
    // build c
    for (var i=0;i<this.m+1;i++) {="" ci="[];" for="" (var="" j="0;j<this.n+1;j++)" ci.push(0);="" this.c.push(ci);="" }="" i="1;i<this.m+1;i++)" if="" (this.x[i-1]="=this.y[j-1])" this.c[i][j]="this.c[i-1][j-1]+1;" else="" this.d="this.c[this.m][this.n];" };="" *="" get="" all="" lcs="" given="" i,j,="" recall="" c[i][j]="" to="" build="" push="" every="" self.r="" @params="" {int}="" i,j="" {string}="" z="" @return="" void="" lcs.prototype.getalllcs="function" (i,j,z)="" (i="=0" ||="" var="" zr;="" (this.islist)="" zr="z.reverse();" (this.r.indexof(zr)<0)="" this.r.push(zr);="" return;="" z.push(this.x[i-1]);="" this.getalllcs(i-1,j-1,z);="" this.getalllcs(i-1,j-1,z+this.x[i-1]);="" (this.c[i-1][j]="">this.c[i][j-1]) this.getAllLCS(i-1,j,z);
    else if (this.c[i-1][j]<this.c[i][j-1]) 2="" this.getalllcs(i,j-1,z);="" else="" {="" var="" tmp;="" if="" (this.islist)="" tmp="z.slice(0);" this.getalllcs(i-1,j,z);="" this.getalllcs(i,j-1,tmp);="" }="" };="" *="" calculate="" the="" edit-distance="" of="" strings="" 0:="" same="" longer:="" less="" similar="" @params="" @return="" function="" editdistance(x,y)="" m="x.length;" n="y.length;" e="[];" 空串的情况先赋值，i="">0,j>0会重新赋值，先不用管
    for (i=0;i<m+1;i++) 2="" {="" ei="[];" for="" (j="0;j<n+1;j++)" ei.push(i+j);="" e.push(ei);="" }="" (i="1;i<m+1;i++)" var="" a="e[i-1][j]+1;" b="e[i][j-1]+1;" if="" (x[i-1]="=y[j-1])" c="e[i-1][j-1];" else="" e[i][j]="Math.min(a,b,c);" return="" e[m][n];="" *="" calculate="" the="" cosine="" similarity="" of="" strings="" 1:="" same="" smaller:="" less="" similar="" distance="1" -="" @params="" {list}="" x,y="" @return="" {float}="" function="" cossim(x,y)="" (x.length="" !="y.length)" alert('different="" list="" length!');="" return;="" product="0" (var="" i="0;i<x.length;i++)" +="x[i]*y[i];" math.sqrt(a)="" math.sqrt(b);="" get="" ngram="" string="" ngram(s,n)="" (!n)="" n="2;" m="s.length;" if(n="">m || n</m+1;i++)></this.c[i][j-1])></this.m+1;i++)>