namu_lfmt.py
=========
## 1. Usage
`$ ./namu_lfmt.py < input.txt > output.txt`  
## 2. Syntax
`{NAME}` starts coloring.  
ALL: `{}`  
베이비소울: `{베이비소울}`, `{소울}`, `{1}`  
유지애: `{유지애}`, `{지애}`, `{2}`  
서지수: `{서지수}`, `{지수}`, `{3}`  
이미주: `{이미주}`, `{미주}`, `{4}`  
Kei: `{Kei}`, `{케이}`, `{5}`  
JIN: `{JIN}`, `{명은}`, `{6}`  
류수정: `{류수정}`, `{수정}`, `{7}`  
정예인: `{정예인}`, `{예인}`, `{8}`  
## 3. Example
```
{수정}기억 속 널 삼킨다
{}Obliviate Obliviate
{예인}너를 잊는다
{}Obliviate Obliviate
{케이}보내줄게 이제 안녕 너로 가득한 지난날
{미주}영원히 널 모두 잊는다

{명은}Don't take me down down
Stop it Down down
Stop it down down
Stop it {지수}(All day long)
{수정}Let me down down
Stop it down down stop it
{예인}영원히 널 모두 잊는다

```
will be converted to
```
{{{#31CED2 기억 속 널 삼킨다}}}
Obliviate Obliviate
{{{#4EC32A 너를 잊는다}}}
Obliviate Obliviate
{{{#EC005F 보내줄게 이제 안녕 너로 가득한 지난날}}}
{{{#FF7D91 영원히 널 모두 잊는다}}}

{{{#EC3B00 Don't take me down down
Stop it Down down
Stop it down down
Stop it}}} {{{#8F28BD (All day long)}}}
{{{#31CED2 Let me down down
Stop it down down stop it}}}
{{{#4EC32A 영원히 널 모두 잊는다}}}
```
