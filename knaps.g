grammar knaps;

options {
    language=Python3;
}

@members {
    global data
    # dicts are mutable in Python, which allows referencing this var via parser
    data = {}
}

/*
 * Parser Rules
 */

we returns [data=data] : items NEWLINE values NEWLINE bag EOF ;

items : PRZEDMIOTY NEWLINE (ite)+ '.' ;

ite : ID '(' NUMBER ')' {data[$ID.text] = {'weight': $NUMBER.int}} (COMMA)? ;

values : WARTOSCI NEWLINE val (COMMA NEWLINE val)* '.' ;

val : WART '(' ID ')' '=' NUMBER {data[$ID.text].update( {'value': $NUMBER.int} )}
{data[$ID.text].update( {'dependencies': []} )
data[$ID.text].update( {'dep_value': $NUMBER.int})}
(JESLI JEST '(' dep_parser {data[$ID.text]['dependencies'] = $dep_parser.dependencies} ')' (NEWLINE)? INACZEJ NUMBER
{data[$ID.text]['dep_value'] = data[$ID.text]['value']
data[$ID.text]['value'] = $NUMBER.int}
)? ;

dep_parser returns [dependencies=[]] : (dep_or {$dependencies.append($dep_or.value)})+ ;

dep_or returns [value=[]] : (dep | dep_plus )
{if $dep.text:
    $value = $dep.value
else:
    $value = $dep_plus.value}
(LUB)? ;

dep returns [value] : ID {$value = $ID.text} ;

dep_plus returns [value=set()] : ID {$value.add($ID.text)} I ID {$value.add($ID.text)} ;

bag returns [value] : PLECAK NUMBER {$value = $NUMBER.int} '.' ;

/*
 * Lexer Rules
 */

PRZEDMIOTY : [pP]'rzedmioty' ':';

WARTOSCI : [wW]'artosci' ':' ;

PLECAK : [pP]'lecak' ':' ;

NUMBER : [0-9]+ ;

WART : 'wartosc' ;

I : 'i' ;

LUB : 'lub' ;

JESLI : 'jesli' ;

JEST : 'jest' ;

INACZEJ : 'inaczej' ;

COMMA : ',' ;

ID : [a-zA-Z]+ ;

NEWLINE : '\r' '\n' | '\n' | '\r' ;

WHITESPACE : ( '\t' | ' ' | '\u000C' ) -> skip ;
