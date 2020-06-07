# Generated from knaps.g by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("p\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\6\3!\n\3\r\3\16\3\"\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5\65")
        buf.write("\n\5\f\5\16\58\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6K\n\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6Q\n\6\3\7\3\7\3\7\6\7V\n\7\r\7\16\7W\3\b\3\b")
        buf.write("\5\b\\\n\b\3\b\3\b\5\b`\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\2\2\f\2\4\6\b")
        buf.write("\n\f\16\20\22\24\2\2\2m\2\26\3\2\2\2\4\35\3\2\2\2\6&\3")
        buf.write("\2\2\2\b.\3\2\2\2\n;\3\2\2\2\fU\3\2\2\2\16[\3\2\2\2\20")
        buf.write("a\3\2\2\2\22d\3\2\2\2\24j\3\2\2\2\26\27\5\4\3\2\27\30")
        buf.write("\7\23\2\2\30\31\5\b\5\2\31\32\7\23\2\2\32\33\5\24\13\2")
        buf.write("\33\34\7\2\2\3\34\3\3\2\2\2\35\36\7\7\2\2\36 \7\23\2\2")
        buf.write("\37!\5\6\4\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2")
        buf.write("\2\2#$\3\2\2\2$%\7\3\2\2%\5\3\2\2\2&\'\7\22\2\2\'(\7\4")
        buf.write("\2\2()\7\n\2\2)*\7\5\2\2*,\b\4\1\2+-\7\21\2\2,+\3\2\2")
        buf.write("\2,-\3\2\2\2-\7\3\2\2\2./\7\b\2\2/\60\7\23\2\2\60\66\5")
        buf.write("\n\6\2\61\62\7\21\2\2\62\63\7\23\2\2\63\65\5\n\6\2\64")
        buf.write("\61\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67")
        buf.write("9\3\2\2\28\66\3\2\2\29:\7\3\2\2:\t\3\2\2\2;<\7\13\2\2")
        buf.write("<=\7\4\2\2=>\7\22\2\2>?\7\5\2\2?@\7\6\2\2@A\7\n\2\2AB")
        buf.write("\b\6\1\2BP\b\6\1\2CD\7\16\2\2DE\7\17\2\2EF\7\4\2\2FG\5")
        buf.write("\f\7\2GH\b\6\1\2HJ\7\5\2\2IK\7\23\2\2JI\3\2\2\2JK\3\2")
        buf.write("\2\2KL\3\2\2\2LM\7\20\2\2MN\7\n\2\2NO\b\6\1\2OQ\3\2\2")
        buf.write("\2PC\3\2\2\2PQ\3\2\2\2Q\13\3\2\2\2RS\5\16\b\2ST\b\7\1")
        buf.write("\2TV\3\2\2\2UR\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X")
        buf.write("\r\3\2\2\2Y\\\5\20\t\2Z\\\5\22\n\2[Y\3\2\2\2[Z\3\2\2\2")
        buf.write("\\]\3\2\2\2]_\b\b\1\2^`\7\r\2\2_^\3\2\2\2_`\3\2\2\2`\17")
        buf.write("\3\2\2\2ab\7\22\2\2bc\b\t\1\2c\21\3\2\2\2de\7\22\2\2e")
        buf.write("f\b\n\1\2fg\7\f\2\2gh\7\22\2\2hi\b\n\1\2i\23\3\2\2\2j")
        buf.write("k\7\t\2\2kl\7\n\2\2lm\b\13\1\2mn\7\3\2\2n\25\3\2\2\2\n")
        buf.write("\",\66JPW[_")
        return buf.getvalue()


class knapsParser ( Parser ):

    grammarFileName = "knaps.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'('", "')'", "'='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'wartosc'", 
                     "'i'", "'lub'", "'jesli'", "'jest'", "'inaczej'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PRZEDMIOTY", "WARTOSCI", "PLECAK", "NUMBER", 
                      "WART", "I", "LUB", "JESLI", "JEST", "INACZEJ", "COMMA", 
                      "ID", "NEWLINE", "WHITESPACE" ]

    RULE_we = 0
    RULE_items = 1
    RULE_ite = 2
    RULE_values = 3
    RULE_val = 4
    RULE_dep_parser = 5
    RULE_dep_or = 6
    RULE_dep = 7
    RULE_dep_plus = 8
    RULE_bag = 9

    ruleNames =  [ "we", "items", "ite", "values", "val", "dep_parser", 
                   "dep_or", "dep", "dep_plus", "bag" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    PRZEDMIOTY=5
    WARTOSCI=6
    PLECAK=7
    NUMBER=8
    WART=9
    I=10
    LUB=11
    JESLI=12
    JEST=13
    INACZEJ=14
    COMMA=15
    ID=16
    NEWLINE=17
    WHITESPACE=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        global data
        # dicts are mutable in Python, which allows referencing this var via parser
        data = {}



    class WeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = data

        def items(self):
            return self.getTypedRuleContext(knapsParser.ItemsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(knapsParser.NEWLINE)
            else:
                return self.getToken(knapsParser.NEWLINE, i)

        def values(self):
            return self.getTypedRuleContext(knapsParser.ValuesContext,0)


        def bag(self):
            return self.getTypedRuleContext(knapsParser.BagContext,0)


        def EOF(self):
            return self.getToken(knapsParser.EOF, 0)

        def getRuleIndex(self):
            return knapsParser.RULE_we

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWe" ):
                listener.enterWe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWe" ):
                listener.exitWe(self)




    def we(self):

        localctx = knapsParser.WeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_we)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.items()
            self.state = 21
            self.match(knapsParser.NEWLINE)
            self.state = 22
            self.values()
            self.state = 23
            self.match(knapsParser.NEWLINE)
            self.state = 24
            self.bag()
            self.state = 25
            self.match(knapsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRZEDMIOTY(self):
            return self.getToken(knapsParser.PRZEDMIOTY, 0)

        def NEWLINE(self):
            return self.getToken(knapsParser.NEWLINE, 0)

        def ite(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(knapsParser.IteContext)
            else:
                return self.getTypedRuleContext(knapsParser.IteContext,i)


        def getRuleIndex(self):
            return knapsParser.RULE_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItems" ):
                listener.enterItems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItems" ):
                listener.exitItems(self)




    def items(self):

        localctx = knapsParser.ItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_items)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(knapsParser.PRZEDMIOTY)
            self.state = 28
            self.match(knapsParser.NEWLINE)
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self.ite()
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==knapsParser.ID):
                    break

            self.state = 34
            self.match(knapsParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._NUMBER = None # Token

        def ID(self):
            return self.getToken(knapsParser.ID, 0)

        def NUMBER(self):
            return self.getToken(knapsParser.NUMBER, 0)

        def COMMA(self):
            return self.getToken(knapsParser.COMMA, 0)

        def getRuleIndex(self):
            return knapsParser.RULE_ite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIte" ):
                listener.enterIte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIte" ):
                listener.exitIte(self)




    def ite(self):

        localctx = knapsParser.IteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            localctx._ID = self.match(knapsParser.ID)
            self.state = 37
            self.match(knapsParser.T__1)
            self.state = 38
            localctx._NUMBER = self.match(knapsParser.NUMBER)
            self.state = 39
            self.match(knapsParser.T__2)
            data[(None if localctx._ID is None else localctx._ID.text)] = {'weight': (0 if localctx._NUMBER is None else int(localctx._NUMBER.text))}
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==knapsParser.COMMA:
                self.state = 41
                self.match(knapsParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WARTOSCI(self):
            return self.getToken(knapsParser.WARTOSCI, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(knapsParser.NEWLINE)
            else:
                return self.getToken(knapsParser.NEWLINE, i)

        def val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(knapsParser.ValContext)
            else:
                return self.getTypedRuleContext(knapsParser.ValContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(knapsParser.COMMA)
            else:
                return self.getToken(knapsParser.COMMA, i)

        def getRuleIndex(self):
            return knapsParser.RULE_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues" ):
                listener.enterValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues" ):
                listener.exitValues(self)




    def values(self):

        localctx = knapsParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(knapsParser.WARTOSCI)
            self.state = 45
            self.match(knapsParser.NEWLINE)
            self.state = 46
            self.val()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==knapsParser.COMMA:
                self.state = 47
                self.match(knapsParser.COMMA)
                self.state = 48
                self.match(knapsParser.NEWLINE)
                self.state = 49
                self.val()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(knapsParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._NUMBER = None # Token
            self._dep_parser = None # Dep_parserContext

        def WART(self):
            return self.getToken(knapsParser.WART, 0)

        def ID(self):
            return self.getToken(knapsParser.ID, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(knapsParser.NUMBER)
            else:
                return self.getToken(knapsParser.NUMBER, i)

        def JESLI(self):
            return self.getToken(knapsParser.JESLI, 0)

        def JEST(self):
            return self.getToken(knapsParser.JEST, 0)

        def dep_parser(self):
            return self.getTypedRuleContext(knapsParser.Dep_parserContext,0)


        def INACZEJ(self):
            return self.getToken(knapsParser.INACZEJ, 0)

        def NEWLINE(self):
            return self.getToken(knapsParser.NEWLINE, 0)

        def getRuleIndex(self):
            return knapsParser.RULE_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVal" ):
                listener.enterVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVal" ):
                listener.exitVal(self)




    def val(self):

        localctx = knapsParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(knapsParser.WART)
            self.state = 58
            self.match(knapsParser.T__1)
            self.state = 59
            localctx._ID = self.match(knapsParser.ID)
            self.state = 60
            self.match(knapsParser.T__2)
            self.state = 61
            self.match(knapsParser.T__3)
            self.state = 62
            localctx._NUMBER = self.match(knapsParser.NUMBER)
            data[(None if localctx._ID is None else localctx._ID.text)].update( {'value': (0 if localctx._NUMBER is None else int(localctx._NUMBER.text))} )
            data[(None if localctx._ID is None else localctx._ID.text)].update( {'dependencies': []} )
            data[(None if localctx._ID is None else localctx._ID.text)].update( {'dep_value': (0 if localctx._NUMBER is None else int(localctx._NUMBER.text))})
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==knapsParser.JESLI:
                self.state = 65
                self.match(knapsParser.JESLI)
                self.state = 66
                self.match(knapsParser.JEST)
                self.state = 67
                self.match(knapsParser.T__1)
                self.state = 68
                localctx._dep_parser = self.dep_parser()
                data[(None if localctx._ID is None else localctx._ID.text)]['dependencies'] = localctx._dep_parser.dependencies
                self.state = 70
                self.match(knapsParser.T__2)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==knapsParser.NEWLINE:
                    self.state = 71
                    self.match(knapsParser.NEWLINE)


                self.state = 74
                self.match(knapsParser.INACZEJ)
                self.state = 75
                localctx._NUMBER = self.match(knapsParser.NUMBER)
                data[(None if localctx._ID is None else localctx._ID.text)]['dep_value'] = data[(None if localctx._ID is None else localctx._ID.text)]['value']
                data[(None if localctx._ID is None else localctx._ID.text)]['value'] = (0 if localctx._NUMBER is None else int(localctx._NUMBER.text))


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dep_parserContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.dependencies = []
            self._dep_or = None # Dep_orContext

        def dep_or(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(knapsParser.Dep_orContext)
            else:
                return self.getTypedRuleContext(knapsParser.Dep_orContext,i)


        def getRuleIndex(self):
            return knapsParser.RULE_dep_parser

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDep_parser" ):
                listener.enterDep_parser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDep_parser" ):
                listener.exitDep_parser(self)




    def dep_parser(self):

        localctx = knapsParser.Dep_parserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dep_parser)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                localctx._dep_or = self.dep_or()
                localctx.dependencies.append(localctx._dep_or.value)
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==knapsParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dep_orContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = []
            self._dep = None # DepContext
            self._dep_plus = None # Dep_plusContext

        def dep(self):
            return self.getTypedRuleContext(knapsParser.DepContext,0)


        def dep_plus(self):
            return self.getTypedRuleContext(knapsParser.Dep_plusContext,0)


        def LUB(self):
            return self.getToken(knapsParser.LUB, 0)

        def getRuleIndex(self):
            return knapsParser.RULE_dep_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDep_or" ):
                listener.enterDep_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDep_or" ):
                listener.exitDep_or(self)




    def dep_or(self):

        localctx = knapsParser.Dep_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dep_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 87
                localctx._dep = self.dep()
                pass

            elif la_ == 2:
                self.state = 88
                localctx._dep_plus = self.dep_plus()
                pass


            if (None if localctx._dep is None else self._input.getText(localctx._dep.start,localctx._dep.stop)):
                localctx.value = localctx._dep.value
            else:
                localctx.value = localctx._dep_plus.value
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==knapsParser.LUB:
                self.state = 92
                self.match(knapsParser.LUB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DepContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self._ID = None # Token

        def ID(self):
            return self.getToken(knapsParser.ID, 0)

        def getRuleIndex(self):
            return knapsParser.RULE_dep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDep" ):
                listener.enterDep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDep" ):
                listener.exitDep(self)




    def dep(self):

        localctx = knapsParser.DepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            localctx._ID = self.match(knapsParser.ID)
            localctx.value = (None if localctx._ID is None else localctx._ID.text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dep_plusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = set()
            self._ID = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(knapsParser.ID)
            else:
                return self.getToken(knapsParser.ID, i)

        def I(self):
            return self.getToken(knapsParser.I, 0)

        def getRuleIndex(self):
            return knapsParser.RULE_dep_plus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDep_plus" ):
                listener.enterDep_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDep_plus" ):
                listener.exitDep_plus(self)




    def dep_plus(self):

        localctx = knapsParser.Dep_plusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dep_plus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            localctx._ID = self.match(knapsParser.ID)
            localctx.value.add((None if localctx._ID is None else localctx._ID.text))
            self.state = 100
            self.match(knapsParser.I)
            self.state = 101
            localctx._ID = self.match(knapsParser.ID)
            localctx.value.add((None if localctx._ID is None else localctx._ID.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self._NUMBER = None # Token

        def PLECAK(self):
            return self.getToken(knapsParser.PLECAK, 0)

        def NUMBER(self):
            return self.getToken(knapsParser.NUMBER, 0)

        def getRuleIndex(self):
            return knapsParser.RULE_bag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBag" ):
                listener.enterBag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBag" ):
                listener.exitBag(self)




    def bag(self):

        localctx = knapsParser.BagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(knapsParser.PLECAK)
            self.state = 105
            localctx._NUMBER = self.match(knapsParser.NUMBER)
            localctx.value = (0 if localctx._NUMBER is None else int(localctx._NUMBER.text))
            self.state = 107
            self.match(knapsParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





