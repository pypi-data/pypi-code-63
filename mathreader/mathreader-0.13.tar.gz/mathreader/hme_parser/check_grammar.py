from mathreader import helpers
from mathreader.hme_parser import check_grammar_lex as check_grammar_lex
from mathreader.hme_parser import check_grammar_yacc as check_grammar_yacc
from mathreader.helpers.exceptions import GrammarError, LexicalError, SintaticError
import numpy as np


class CheckGrammar():

    def __init__(self):
        self.__attempts_lex = 0
        self.__attempts_grammar = 0

    def check(self, latex_data):
        """
        Returns:
            {
                'latex': self.latex,
                'latex_list': self.latex_list,
                'latex_string': self.latex_string,
                'yacc_errors_history': self.yacc_errors_history,
                'lex_errors_history': self.lex_errors_history,
                'yacc_pure_errors': self.pure_yacc_errors,
                'lex_pure_errors': self.pure_lex_errors # Não está sendo adicionado aqui
            }
        """
        helpers.debug("[check_grammar.py] check()")
        helpers.debug("[check_grammar.py] latex_data: {0}".format(latex_data))

        latex = latex_data['latex']
        latex_list = latex_data['latex_list']
        latex_string = latex_data['latex_string']
        lstring = latex_data['lstring']

        helpers.debug("[check_grammar.py] check() | Latex List:")
        helpers.debug(latex_list)
        helpers.debug("[check_grammar.py] check() | \
            Latex String: %s " % latex_string)

        try:
            check_lex_data = self.__check_lex(latex_string, latex, latex_list)
            check_yacc_data = self.__check_yacc(check_lex_data)

            if check_lex_data['latex_string'] != -1 and \
            check_lex_data['latex_string'] is not None:

                lstring = check_lex_data['latex_string']

            check_yacc_data.update({'latex_string_original': latex_string})

            return check_yacc_data

        except (GrammarError, SintaticError, LexicalError) as e:
            e.data.update({'latex_string_original': latex_string})
            raise e

        except BaseException as e:
            raise e

    def __check_lex(self, latex_string, latex, latex_list):
        cgl = check_grammar_lex.CheckLex()

        cgl.latex_string = latex_string
        cgl.latex = latex
        cgl.latex_list = latex_list
        cgl.attempts = self.__attempts_lex

        check_lex_data = cgl.check_correct_lex()

        return check_lex_data

    def __check_yacc(self, check_lex_data=None):
        """
        Returns:
            {
                'latex': self.latex,
                'latex_list': self.latex_list,
                'latex_string': self.latex_string,
                'yacc_errors_history': self.yacc_errors_history,
                'lex_errors_history': self.lex_errors_history,
                'yacc_pure_errors': self.pure_yacc_errors,
                'lex_pure_errors': self.pure_lex_errors # Não está sendo adicionado aqui
            }
        """

        helpers.debug('[check_grammar.py] __check_yacc()')
        helpers.debug('[check_grammar.py] __check_yacc() | \
            before CheckSintax() ')

        cgs = check_grammar_yacc.CheckSintax()
        cgs.attempts = self.__attempts_grammar

        if check_lex_data:
            cgs.set_lex_data(check_lex_data)

        check_data_yacc = cgs.check_correct_grammar()

        return check_data_yacc


if __name__ == "__main__":
    """ For debugging purposes """

    latex_data1 = {
       'latex': [
            {'label': '0', 'prediction': np.array([[9.9974996e-01, 2.4048815e-05, 5.5696987e-06, 8.8894776e-06,
                3.2870691e-06, 1.4715235e-05, 2.2317370e-05, 5.7810475e-06,
                7.3667557e-06, 6.1125866e-06, 1.8079985e-05, 6.0721482e-06,
                2.6263217e-06, 2.3751154e-06, 4.0072528e-06, 1.9813034e-07,
                1.0582427e-06, 8.7215158e-06, 9.3814269e-06, 1.8223645e-05,
                1.0331525e-05, 4.9983341e-06, 2.4594756e-05, 6.3485418e-06,
                1.0287620e-06, 2.1284319e-05, 8.7481631e-06, 5.6424051e-07,
                1.9102072e-06, 1.3891712e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '.', 'prediction': np.array([[2.0557144e-03, 9.8894397e-04, 4.7322208e-04, 1.1302407e-04,
                6.9213129e-04, 3.4101962e-04, 1.5486331e-03, 2.3203556e-04,
                5.3205690e-04, 6.6061929e-04, 5.6127581e-04, 1.9467773e-03,
                1.9654684e-04, 2.6003682e-04, 5.9470163e-05, 3.7359339e-04,
                1.0754965e-04, 3.3119600e-04, 1.7362378e-03, 1.5016444e-04,
                3.0280551e-04, 2.7806733e-03, 4.4046977e-04, 6.6474796e-04,
                4.1395871e-04, 7.1280502e-04, 5.6821859e-04, 6.0596084e-04,
                9.7934794e-01, 8.0218376e-04]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': 'y', 'prediction': np.array([[8.7034347e-04, 2.5192020e-03, 9.1366930e-04, 5.7303830e-04,
                1.1219951e-01, 7.9176860e-04, 7.2764597e-05, 1.0741318e-03,
                2.6928668e-04, 2.9279746e-03, 4.1475683e-04, 5.9631496e-04,
                8.0790673e-04, 4.9040606e-05, 3.3872391e-04, 6.4053063e-05,
                2.3962965e-04, 2.8913675e-04, 3.4180728e-03, 3.5695471e-03,
                3.4905231e-04, 2.0835490e-04, 2.3474717e-03, 4.5104709e-05,
                1.3224641e-03, 8.6296958e-01, 1.8796140e-04, 1.1195231e-04,
                7.7735458e-05, 3.8151492e-04]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '2', 'prediction': np.array([[3.56128803e-05, 9.25179847e-05, 9.99069154e-01, 3.33975040e-05,
                2.13432177e-05, 1.49486295e-05, 2.28315093e-05, 9.00378836e-06,
                8.90851970e-06, 6.81503116e-06, 3.48807989e-05, 7.52042615e-05,
                4.26850347e-05, 1.07086626e-05, 1.36013323e-05, 4.52336235e-06,
                5.64377558e-07, 1.43096304e-05, 2.65613693e-04, 3.64512598e-05,
                2.34587405e-05, 4.31694707e-06, 2.88743158e-05, 7.53296945e-06,
                5.93014738e-05, 7.78605317e-06, 4.71818748e-05, 4.48556619e-07,
                1.94900599e-06, 6.09833069e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '9', 'prediction': np.array([[6.5626438e-08, 1.2683070e-07, 2.5831042e-08, 1.5874384e-07,
                1.5190871e-07, 1.5565311e-07, 3.3196115e-09, 4.7002203e-08,
                8.9629552e-08, 9.9999845e-01, 5.8725139e-08, 5.1741690e-08,
                3.5831791e-09, 6.7577743e-09, 3.4441485e-09, 6.7909305e-09,
                2.4015110e-09, 1.6146464e-09, 1.7274489e-07, 3.4194456e-09,
                4.6642477e-08, 7.3247293e-09, 3.8944947e-08, 2.4832657e-08,
                3.5860456e-08, 2.6037523e-07, 5.9730842e-09, 6.0646183e-11,
                3.0081985e-08, 1.0530941e-09]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '7', 'prediction': np.array([[1.3700732e-05, 1.9077774e-05, 8.0076707e-06, 2.1669468e-05,
                1.0107856e-05, 2.1101032e-06, 5.0092922e-07, 9.9974698e-01,
                5.0240974e-06, 1.9098416e-05, 7.5215348e-06, 3.9518959e-06,
                6.9201951e-06, 2.6749458e-06, 1.9972942e-05, 2.7079113e-07,
                6.9309573e-07, 5.6159415e-06, 6.4315100e-06, 5.8422313e-07,
                6.3680118e-06, 2.6130556e-06, 3.1117956e-06, 1.4503828e-06,
                1.0562488e-05, 3.6865949e-06, 5.6714402e-05, 1.3953164e-05,
                6.8752193e-08, 5.1757132e-07]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '-', 'prediction': np.array([[8.4389765e-05, 1.7255115e-05, 3.3016699e-05, 1.0484437e-05,
                6.6803972e-05, 5.5382461e-06, 7.5987450e-06, 5.1861948e-06,
                1.9811848e-06, 8.1837406e-06, 9.9959153e-01, 1.0345957e-05,
                7.7403811e-06, 2.0518225e-06, 3.2858741e-06, 3.8217905e-07,
                8.7386599e-07, 1.8271883e-05, 5.6096920e-05, 5.1794927e-06,
                2.1336675e-06, 1.4508982e-05, 1.0110583e-05, 2.0728741e-05,
                2.9912633e-06, 2.4887074e-06, 7.2238545e-06, 7.5647142e-07,
                3.5650601e-07, 2.5349700e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '0', 'prediction': np.array([[9.9439585e-01, 1.6420976e-04, 2.5096614e-04, 1.3671340e-04,
                5.9841732e-05, 1.3445900e-04, 3.2883370e-04, 6.4382482e-05,
                1.8957147e-04, 1.0988204e-04, 3.1585316e-04, 1.6447526e-04,
                3.0527466e-05, 3.9687257e-05, 5.8256155e-05, 7.1190084e-06,
                1.3486231e-05, 1.4405095e-04, 2.5602048e-03, 1.2573323e-04,
                1.7669330e-04, 4.6330391e-05, 1.1271719e-04, 8.4505773e-05,
                3.0732903e-05, 1.0861317e-04, 2.9390860e-05, 6.9209104e-06,
                9.8160141e-05, 1.1949505e-05]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '.', 'prediction': np.array([[1.48911888e-04, 4.37413291e-05, 4.22927733e-05, 4.56826820e-06,
                1.00949648e-04, 2.20247275e-05, 1.07728047e-04, 1.47596929e-05,
                5.16946966e-05, 7.67944075e-05, 3.13545388e-05, 1.01903868e-04,
                9.90288754e-06, 1.52249495e-05, 2.29445345e-06, 3.34571996e-05,
                1.01620426e-05, 1.10258825e-05, 3.25761648e-04, 8.50803463e-06,
                2.33041592e-05, 1.35001348e-04, 2.14322808e-05, 3.92156435e-05,
                1.23987420e-05, 7.83846699e-05, 7.44266581e-05, 1.14673885e-05,
                9.98402894e-01, 3.84542473e-05]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '4', 'prediction': np.array([[1.5395038e-03, 3.9682430e-03, 1.7762521e-02, 1.7406892e-03,
                8.1947571e-01, 3.6259447e-03, 1.2859057e-02, 1.7236513e-03,
                1.7375594e-03, 2.7986257e-03, 2.8872718e-03, 8.6718295e-03,
                2.4946185e-03, 9.6023059e-04, 1.1841025e-03, 7.6949247e-04,
                1.1673279e-03, 1.3112035e-02, 2.1435623e-03, 7.9579882e-02,
                5.1837568e-03, 8.0816657e-04, 2.3774956e-03, 1.3863564e-03,
                1.3504807e-03, 3.0953686e-03, 1.4726813e-03, 1.5904875e-03,
                1.2298918e-03, 1.3034616e-03]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '+', 'prediction': np.array([[3.07101509e-05, 6.77146018e-05, 3.29303475e-05, 2.84802827e-05,
                1.12610440e-04, 2.56905842e-05, 1.46958500e-05, 3.61185885e-05,
                1.03675684e-05, 5.61048046e-06, 1.91639949e-04, 4.21012883e-05,
                2.91377164e-05, 5.41926829e-06, 1.10699502e-05, 5.95196934e-06,
                1.02363319e-05, 9.98987257e-01, 1.24540920e-05, 3.18662751e-05,
                1.20160985e-05, 9.41848430e-06, 2.76465053e-05, 3.54088770e-05,
                4.21612349e-05, 4.60960327e-05, 2.13500389e-05, 5.89017473e-05,
                2.62973231e-06, 5.23353665e-05]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '2', 'prediction': np.array([[2.9589617e-05, 4.3491931e-05, 9.9882883e-01, 2.3764385e-05,
                1.3054997e-05, 1.4765088e-05, 2.3583612e-05, 1.5974174e-05,
                1.4258368e-05, 4.8979168e-06, 2.9061113e-05, 3.4686698e-05,
                2.1269130e-05, 1.7069442e-05, 1.0087668e-05, 2.5816755e-06,
                5.0258996e-07, 1.4103236e-05, 1.9944337e-04, 2.1158708e-05,
                3.3662011e-05, 4.4446583e-06, 7.2169016e-05, 5.3051713e-06,
                2.5536044e-04, 4.5763977e-06, 2.5703508e-04, 3.0551197e-07,
                8.2016498e-07, 4.0310456e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '.', 'prediction': np.array([[9.8070269e-03, 2.6664785e-03, 2.8009966e-03, 8.2349189e-04,
                3.4427166e-03, 1.0510056e-03, 4.4535026e-03, 8.9771254e-04,
                5.5321394e-03, 2.4106929e-03, 2.1339557e-03, 3.6474187e-03,
                9.3220785e-04, 1.3363203e-03, 5.9157668e-04, 3.0518703e-03,
                7.2112319e-04, 1.0832053e-03, 2.7818248e-02, 9.7179238e-04,
                2.1179833e-03, 1.0025238e-02, 1.6402962e-03, 3.7556302e-03,
                9.7635266e-04, 3.9882413e-03, 1.7631381e-03, 3.0958296e-03,
                8.8935190e-01, 7.1120202e-03]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '0', 'prediction': np.array([[9.94274318e-01, 1.90027204e-04, 1.11099485e-04, 1.32014713e-04,
                6.03598091e-05, 1.53986955e-04, 1.01985340e-03, 5.59141117e-05,
                2.69676995e-04, 9.24895357e-05, 3.20346764e-04, 2.11196835e-04,
                4.60514530e-05, 4.90415296e-05, 4.95936874e-05, 8.59268312e-06,
                2.47093958e-05, 8.97291247e-05, 1.51941110e-03, 4.77592635e-04,
                2.13305815e-04, 6.64810141e-05, 9.68105087e-05, 1.49815547e-04,
                3.58933794e-05, 1.17513438e-04, 6.37744306e-05, 1.35416221e-05,
                7.58659371e-05, 1.10383289e-05]], dtype=np.float32), 'type': 'Normal'}
        ], 
        'latex_list': ['0', '.', 'y', '2', '9', '7', '-', '0', '.', '4', '+', '2', '.', '0'], 
        'latex_string': '0.y297-0.4+2.0', 
        'lstring': '0.y297-0.4+2.0'
    }

    latex_data2 = {
        'latex': [
            {'label': '0', 'prediction': np.array([[9.9974996e-01, 2.4048815e-05, 5.5696987e-06, 8.8894776e-06,
                3.2870691e-06, 1.4715235e-05, 2.2317370e-05, 5.7810475e-06,
                7.3667557e-06, 6.1125866e-06, 1.8079985e-05, 6.0721482e-06,
                2.6263217e-06, 2.3751154e-06, 4.0072528e-06, 1.9813034e-07,
                1.0582427e-06, 8.7215158e-06, 9.3814269e-06, 1.8223645e-05,
                1.0331525e-05, 4.9983341e-06, 2.4594756e-05, 6.3485418e-06,
                1.0287620e-06, 2.1284319e-05, 8.7481631e-06, 5.6424051e-07,
                1.9102072e-06, 1.3891712e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '.', 'prediction': np.array([[2.0557144e-03, 9.8894397e-04, 4.7322208e-04, 1.1302407e-04,
                6.9213129e-04, 3.4101962e-04, 1.5486331e-03, 2.3203556e-04,
                5.3205690e-04, 6.6061929e-04, 5.6127581e-04, 1.9467773e-03,
                1.9654684e-04, 2.6003682e-04, 5.9470163e-05, 3.7359339e-04,
                1.0754965e-04, 3.3119600e-04, 1.7362378e-03, 1.5016444e-04,
                3.0280551e-04, 2.7806733e-03, 4.4046977e-04, 6.6474796e-04,
                4.1395871e-04, 7.1280502e-04, 5.6821859e-04, 6.0596084e-04,
                9.7934794e-01, 8.0218376e-04]], dtype=np.float32), 'type': 'Normal'},
            {'label': '.', 'prediction': np.array([[2.0557144e-03, 9.8894397e-04, 4.7322208e-04, 1.1302407e-04,
                6.9213129e-04, 3.4101962e-04, 1.5486331e-03, 2.3203556e-04,
                5.3205690e-04, 6.6061929e-04, 5.6127581e-04, 1.9467773e-03,
                1.9654684e-04, 2.6003682e-04, 5.9470163e-05, 3.7359339e-04,
                1.0754965e-04, 3.3119600e-04, 1.7362378e-03, 1.5016444e-04,
                3.0280551e-04, 2.7806733e-03, 4.4046977e-04, 6.6474796e-04,
                4.1395871e-04, 7.1280502e-04, 5.6821859e-04, 6.0596084e-04,
                9.7934794e-01, 8.0218376e-04]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': 'y', 'prediction': np.array([[8.7034347e-04, 2.5192020e-03, 9.1366930e-04, 5.7303830e-04,
                1.1219951e-01, 7.9176860e-04, 7.2764597e-05, 1.0741318e-03,
                2.6928668e-04, 2.9279746e-03, 4.1475683e-04, 5.9631496e-04,
                8.0790673e-04, 4.9040606e-05, 3.3872391e-04, 6.4053063e-05,
                2.3962965e-04, 2.8913675e-04, 3.4180728e-03, 3.5695471e-03,
                3.4905231e-04, 2.0835490e-04, 2.3474717e-03, 4.5104709e-05,
                1.3224641e-03, 8.6296958e-01, 1.8796140e-04, 1.1195231e-04,
                7.7735458e-05, 3.8151492e-04]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '2', 'prediction': np.array([[3.56128803e-05, 9.25179847e-05, 9.99069154e-01, 3.33975040e-05,
                2.13432177e-05, 1.49486295e-05, 2.28315093e-05, 9.00378836e-06,
                8.90851970e-06, 6.81503116e-06, 3.48807989e-05, 7.52042615e-05,
                4.26850347e-05, 1.07086626e-05, 1.36013323e-05, 4.52336235e-06,
                5.64377558e-07, 1.43096304e-05, 2.65613693e-04, 3.64512598e-05,
                2.34587405e-05, 4.31694707e-06, 2.88743158e-05, 7.53296945e-06,
                5.93014738e-05, 7.78605317e-06, 4.71818748e-05, 4.48556619e-07,
                1.94900599e-06, 6.09833069e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '9', 'prediction': np.array([[6.5626438e-08, 1.2683070e-07, 2.5831042e-08, 1.5874384e-07,
                1.5190871e-07, 1.5565311e-07, 3.3196115e-09, 4.7002203e-08,
                8.9629552e-08, 9.9999845e-01, 5.8725139e-08, 5.1741690e-08,
                3.5831791e-09, 6.7577743e-09, 3.4441485e-09, 6.7909305e-09,
                2.4015110e-09, 1.6146464e-09, 1.7274489e-07, 3.4194456e-09,
                4.6642477e-08, 7.3247293e-09, 3.8944947e-08, 2.4832657e-08,
                3.5860456e-08, 2.6037523e-07, 5.9730842e-09, 6.0646183e-11,
                3.0081985e-08, 1.0530941e-09]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '7', 'prediction': np.array([[1.3700732e-05, 1.9077774e-05, 8.0076707e-06, 2.1669468e-05,
                1.0107856e-05, 2.1101032e-06, 5.0092922e-07, 9.9974698e-01,
                5.0240974e-06, 1.9098416e-05, 7.5215348e-06, 3.9518959e-06,
                6.9201951e-06, 2.6749458e-06, 1.9972942e-05, 2.7079113e-07,
                6.9309573e-07, 5.6159415e-06, 6.4315100e-06, 5.8422313e-07,
                6.3680118e-06, 2.6130556e-06, 3.1117956e-06, 1.4503828e-06,
                1.0562488e-05, 3.6865949e-06, 5.6714402e-05, 1.3953164e-05,
                6.8752193e-08, 5.1757132e-07]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '-', 'prediction': np.array([[8.4389765e-05, 1.7255115e-05, 3.3016699e-05, 1.0484437e-05,
                6.6803972e-05, 5.5382461e-06, 7.5987450e-06, 5.1861948e-06,
                1.9811848e-06, 8.1837406e-06, 9.9959153e-01, 1.0345957e-05,
                7.7403811e-06, 2.0518225e-06, 3.2858741e-06, 3.8217905e-07,
                8.7386599e-07, 1.8271883e-05, 5.6096920e-05, 5.1794927e-06,
                2.1336675e-06, 1.4508982e-05, 1.0110583e-05, 2.0728741e-05,
                2.9912633e-06, 2.4887074e-06, 7.2238545e-06, 7.5647142e-07,
                3.5650601e-07, 2.5349700e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '0', 'prediction': np.array([[9.9439585e-01, 1.6420976e-04, 2.5096614e-04, 1.3671340e-04,
                5.9841732e-05, 1.3445900e-04, 3.2883370e-04, 6.4382482e-05,
                1.8957147e-04, 1.0988204e-04, 3.1585316e-04, 1.6447526e-04,
                3.0527466e-05, 3.9687257e-05, 5.8256155e-05, 7.1190084e-06,
                1.3486231e-05, 1.4405095e-04, 2.5602048e-03, 1.2573323e-04,
                1.7669330e-04, 4.6330391e-05, 1.1271719e-04, 8.4505773e-05,
                3.0732903e-05, 1.0861317e-04, 2.9390860e-05, 6.9209104e-06,
                9.8160141e-05, 1.1949505e-05]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '.', 'prediction': np.array([[1.48911888e-04, 4.37413291e-05, 4.22927733e-05, 4.56826820e-06,
                1.00949648e-04, 2.20247275e-05, 1.07728047e-04, 1.47596929e-05,
                5.16946966e-05, 7.67944075e-05, 3.13545388e-05, 1.01903868e-04,
                9.90288754e-06, 1.52249495e-05, 2.29445345e-06, 3.34571996e-05,
                1.01620426e-05, 1.10258825e-05, 3.25761648e-04, 8.50803463e-06,
                2.33041592e-05, 1.35001348e-04, 2.14322808e-05, 3.92156435e-05,
                1.23987420e-05, 7.83846699e-05, 7.44266581e-05, 1.14673885e-05,
                9.98402894e-01, 3.84542473e-05]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '4', 'prediction': np.array([[1.5395038e-03, 3.9682430e-03, 1.7762521e-02, 1.7406892e-03,
                8.1947571e-01, 3.6259447e-03, 1.2859057e-02, 1.7236513e-03,
                1.7375594e-03, 2.7986257e-03, 2.8872718e-03, 8.6718295e-03,
                2.4946185e-03, 9.6023059e-04, 1.1841025e-03, 7.6949247e-04,
                1.1673279e-03, 1.3112035e-02, 2.1435623e-03, 7.9579882e-02,
                5.1837568e-03, 8.0816657e-04, 2.3774956e-03, 1.3863564e-03,
                1.3504807e-03, 3.0953686e-03, 1.4726813e-03, 1.5904875e-03,
                1.2298918e-03, 1.3034616e-03]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '+', 'prediction': np.array([[3.07101509e-05, 6.77146018e-05, 3.29303475e-05, 2.84802827e-05,
                1.12610440e-04, 2.56905842e-05, 1.46958500e-05, 3.61185885e-05,
                1.03675684e-05, 5.61048046e-06, 1.91639949e-04, 4.21012883e-05,
                2.91377164e-05, 5.41926829e-06, 1.10699502e-05, 5.95196934e-06,
                1.02363319e-05, 9.98987257e-01, 1.24540920e-05, 3.18662751e-05,
                1.20160985e-05, 9.41848430e-06, 2.76465053e-05, 3.54088770e-05,
                4.21612349e-05, 4.60960327e-05, 2.13500389e-05, 5.89017473e-05,
                2.62973231e-06, 5.23353665e-05]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '2', 'prediction': np.array([[2.9589617e-05, 4.3491931e-05, 9.9882883e-01, 2.3764385e-05,
                1.3054997e-05, 1.4765088e-05, 2.3583612e-05, 1.5974174e-05,
                1.4258368e-05, 4.8979168e-06, 2.9061113e-05, 3.4686698e-05,
                2.1269130e-05, 1.7069442e-05, 1.0087668e-05, 2.5816755e-06,
                5.0258996e-07, 1.4103236e-05, 1.9944337e-04, 2.1158708e-05,
                3.3662011e-05, 4.4446583e-06, 7.2169016e-05, 5.3051713e-06,
                2.5536044e-04, 4.5763977e-06, 2.5703508e-04, 3.0551197e-07,
                8.2016498e-07, 4.0310456e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '.', 'prediction': np.array([[9.8070269e-03, 2.6664785e-03, 2.8009966e-03, 8.2349189e-04,
                3.4427166e-03, 1.0510056e-03, 4.4535026e-03, 8.9771254e-04,
                5.5321394e-03, 2.4106929e-03, 2.1339557e-03, 3.6474187e-03,
                9.3220785e-04, 1.3363203e-03, 5.9157668e-04, 3.0518703e-03,
                7.2112319e-04, 1.0832053e-03, 2.7818248e-02, 9.7179238e-04,
                2.1179833e-03, 1.0025238e-02, 1.6402962e-03, 3.7556302e-03,
                9.7635266e-04, 3.9882413e-03, 1.7631381e-03, 3.0958296e-03,
                8.8935190e-01, 7.1120202e-03]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '0', 'prediction': np.array([[9.94274318e-01, 1.90027204e-04, 1.11099485e-04, 1.32014713e-04,
                6.03598091e-05, 1.53986955e-04, 1.01985340e-03, 5.59141117e-05,
                2.69676995e-04, 9.24895357e-05, 3.20346764e-04, 2.11196835e-04,
                4.60514530e-05, 4.90415296e-05, 4.95936874e-05, 8.59268312e-06,
                2.47093958e-05, 8.97291247e-05, 1.51941110e-03, 4.77592635e-04,
                2.13305815e-04, 6.64810141e-05, 9.68105087e-05, 1.49815547e-04,
                3.58933794e-05, 1.17513438e-04, 6.37744306e-05, 1.35416221e-05,
                7.58659371e-05, 1.10383289e-05]], dtype=np.float32), 'type': 'Normal'}
        ],
        'latex_list': ['0', '.', '.', 'y', '2', '9', '7', '-', '0', '.', '4', '+', '2', '.', '0'],
        'latex_string': '0..y297-0.4+2.0',
        'lstring': '0..y297-0.4+2.0'
    }

    latex_data3 = {
        'latex': [
            {'label': '0', 'prediction': np.array([[9.9974996e-01, 2.4048815e-05, 5.5696987e-06, 8.8894776e-06,
                3.2870691e-06, 1.4715235e-05, 2.2317370e-05, 5.7810475e-06,
                7.3667557e-06, 6.1125866e-06, 1.8079985e-05, 6.0721482e-06,
                2.6263217e-06, 2.3751154e-06, 4.0072528e-06, 1.9813034e-07,
                1.0582427e-06, 8.7215158e-06, 9.3814269e-06, 1.8223645e-05,
                1.0331525e-05, 4.9983341e-06, 2.4594756e-05, 6.3485418e-06,
                1.0287620e-06, 2.1284319e-05, 8.7481631e-06, 5.6424051e-07,
                1.9102072e-06, 1.3891712e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '(', 'prediction': np.array([[2.0557144e-03, 1, 4.7322208e-04, 1.1302407e-04,
                6.9213129e-04, 3.4101962e-04, 1.5486331e-03, 2.3203556e-04,
                5.3205690e-04, 6.6061929e-04, 5.6127581e-04, 1.9467773e-03,
                1.9654684e-04, 2.6003682e-04, 5.9470163e-05, 3.7359339e-04,
                1.0754965e-04, 3.3119600e-04, 1.7362378e-03, 1.5016444e-04,
                3.0280551e-04, 2.7806733e-03, 4.4046977e-04, 6.6474796e-04,
                4.1395871e-04, 7.1280502e-04, 5.6821859e-04, 6.0596084e-04,
                9.7934794e-01, 8.0218376e-04]], dtype=np.float32), 'type': 'Normal'},
            {'label': 'y', 'prediction': np.array([[8.7034347e-04, 2.5192020e-03, 9.1366930e-04, 5.7303830e-04,
                1.1219951e-01, 7.9176860e-04, 7.2764597e-05, 1.0741318e-03,
                2.6928668e-04, 2.9279746e-03, 4.1475683e-04, 5.9631496e-04,
                8.0790673e-04, 4.9040606e-05, 3.3872391e-04, 6.4053063e-05,
                2.3962965e-04, 2.8913675e-04, 3.4180728e-03, 3.5695471e-03,
                3.4905231e-04, 2.0835490e-04, 2.3474717e-03, 4.5104709e-05,
                1.3224641e-03, 8.6296958e-01, 1.8796140e-04, 1.1195231e-04,
                7.7735458e-05, 3.8151492e-04]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '2', 'prediction': np.array([[3.56128803e-05, 9.25179847e-05, 9.99069154e-01, 3.33975040e-05,
                2.13432177e-05, 1.49486295e-05, 2.28315093e-05, 9.00378836e-06,
                8.90851970e-06, 6.81503116e-06, 3.48807989e-05, 7.52042615e-05,
                4.26850347e-05, 1.07086626e-05, 1.36013323e-05, 4.52336235e-06,
                5.64377558e-07, 1.43096304e-05, 2.65613693e-04, 3.64512598e-05,
                2.34587405e-05, 4.31694707e-06, 2.88743158e-05, 7.53296945e-06,
                5.93014738e-05, 7.78605317e-06, 4.71818748e-05, 4.48556619e-07,
                1.94900599e-06, 6.09833069e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '9', 'prediction': np.array([[6.5626438e-08, 1.2683070e-07, 2.5831042e-08, 1.5874384e-07,
                1.5190871e-07, 1.5565311e-07, 3.3196115e-09, 4.7002203e-08,
                8.9629552e-08, 9.9999845e-01, 5.8725139e-08, 5.1741690e-08,
                3.5831791e-09, 6.7577743e-09, 3.4441485e-09, 6.7909305e-09,
                2.4015110e-09, 1.6146464e-09, 1.7274489e-07, 3.4194456e-09,
                4.6642477e-08, 7.3247293e-09, 3.8944947e-08, 2.4832657e-08,
                3.5860456e-08, 2.6037523e-07, 5.9730842e-09, 6.0646183e-11,
                3.0081985e-08, 1.0530941e-09]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '7', 'prediction': np.array([[1.3700732e-05, 1.9077774e-05, 8.0076707e-06, 2.1669468e-05,
                1.0107856e-05, 2.1101032e-06, 5.0092922e-07, 9.9974698e-01,
                5.0240974e-06, 1.9098416e-05, 7.5215348e-06, 3.9518959e-06,
                6.9201951e-06, 2.6749458e-06, 1.9972942e-05, 2.7079113e-07,
                6.9309573e-07, 5.6159415e-06, 6.4315100e-06, 5.8422313e-07,
                6.3680118e-06, 2.6130556e-06, 3.1117956e-06, 1.4503828e-06,
                1.0562488e-05, 3.6865949e-06, 5.6714402e-05, 1.3953164e-05,
                6.8752193e-08, 5.1757132e-07]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '-', 'prediction': np.array([[8.4389765e-05, 1.7255115e-05, 3.3016699e-05, 1.0484437e-05,
                6.6803972e-05, 5.5382461e-06, 7.5987450e-06, 5.1861948e-06,
                1.9811848e-06, 8.1837406e-06, 9.9959153e-01, 1.0345957e-05,
                7.7403811e-06, 2.0518225e-06, 3.2858741e-06, 3.8217905e-07,
                8.7386599e-07, 1.8271883e-05, 5.6096920e-05, 5.1794927e-06,
                2.1336675e-06, 1.4508982e-05, 1.0110583e-05, 2.0728741e-05,
                2.9912633e-06, 2.4887074e-06, 7.2238545e-06, 7.5647142e-07,
                3.5650601e-07, 2.5349700e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '0', 'prediction': np.array([[9.9439585e-01, 1.6420976e-04, 2.5096614e-04, 1.3671340e-04,
                5.9841732e-05, 1.3445900e-04, 3.2883370e-04, 6.4382482e-05,
                1.8957147e-04, 1.0988204e-04, 3.1585316e-04, 1.6447526e-04,
                3.0527466e-05, 3.9687257e-05, 5.8256155e-05, 7.1190084e-06,
                1.3486231e-05, 1.4405095e-04, 2.5602048e-03, 1.2573323e-04,
                1.7669330e-04, 4.6330391e-05, 1.1271719e-04, 8.4505773e-05,
                3.0732903e-05, 1.0861317e-04, 2.9390860e-05, 6.9209104e-06,
                9.8160141e-05, 1.1949505e-05]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '.', 'prediction': np.array([[1.48911888e-04, 4.37413291e-05, 4.22927733e-05, 4.56826820e-06,
                1.00949648e-04, 2.20247275e-05, 1.07728047e-04, 1.47596929e-05,
                5.16946966e-05, 7.67944075e-05, 3.13545388e-05, 1.01903868e-04,
                9.90288754e-06, 1.52249495e-05, 2.29445345e-06, 3.34571996e-05,
                1.01620426e-05, 1.10258825e-05, 3.25761648e-04, 8.50803463e-06,
                2.33041592e-05, 1.35001348e-04, 2.14322808e-05, 3.92156435e-05,
                1.23987420e-05, 7.83846699e-05, 7.44266581e-05, 1.14673885e-05,
                9.98402894e-01, 3.84542473e-05]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '4', 'prediction': np.array([[1.5395038e-03, 3.9682430e-03, 1.7762521e-02, 1.7406892e-03,
                8.1947571e-01, 3.6259447e-03, 1.2859057e-02, 1.7236513e-03,
                1.7375594e-03, 2.7986257e-03, 2.8872718e-03, 8.6718295e-03,
                2.4946185e-03, 9.6023059e-04, 1.1841025e-03, 7.6949247e-04,
                1.1673279e-03, 1.3112035e-02, 2.1435623e-03, 7.9579882e-02,
                5.1837568e-03, 8.0816657e-04, 2.3774956e-03, 1.3863564e-03,
                1.3504807e-03, 3.0953686e-03, 1.4726813e-03, 1.5904875e-03,
                1.2298918e-03, 1.3034616e-03]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '+', 'prediction': np.array([[3.07101509e-05, 6.77146018e-05, 3.29303475e-05, 2.84802827e-05,
                1.12610440e-04, 2.56905842e-05, 1.46958500e-05, 3.61185885e-05,
                1.03675684e-05, 5.61048046e-06, 1.91639949e-04, 4.21012883e-05,
                2.91377164e-05, 5.41926829e-06, 1.10699502e-05, 5.95196934e-06,
                1.02363319e-05, 9.98987257e-01, 1.24540920e-05, 3.18662751e-05,
                1.20160985e-05, 9.41848430e-06, 2.76465053e-05, 3.54088770e-05,
                4.21612349e-05, 4.60960327e-05, 2.13500389e-05, 5.89017473e-05,
                2.62973231e-06, 5.23353665e-05]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '2', 'prediction': np.array([[2.9589617e-05, 4.3491931e-05, 9.9882883e-01, 2.3764385e-05,
                1.3054997e-05, 1.4765088e-05, 2.3583612e-05, 1.5974174e-05,
                1.4258368e-05, 4.8979168e-06, 2.9061113e-05, 3.4686698e-05,
                2.1269130e-05, 1.7069442e-05, 1.0087668e-05, 2.5816755e-06,
                5.0258996e-07, 1.4103236e-05, 1.9944337e-04, 2.1158708e-05,
                3.3662011e-05, 4.4446583e-06, 7.2169016e-05, 5.3051713e-06,
                2.5536044e-04, 4.5763977e-06, 2.5703508e-04, 3.0551197e-07,
                8.2016498e-07, 4.0310456e-06]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '.', 'prediction': np.array([[9.8070269e-03, 2.6664785e-03, 2.8009966e-03, 8.2349189e-04,
                3.4427166e-03, 1.0510056e-03, 4.4535026e-03, 8.9771254e-04,
                5.5321394e-03, 2.4106929e-03, 2.1339557e-03, 3.6474187e-03,
                9.3220785e-04, 1.3363203e-03, 5.9157668e-04, 3.0518703e-03,
                7.2112319e-04, 1.0832053e-03, 2.7818248e-02, 9.7179238e-04,
                2.1179833e-03, 1.0025238e-02, 1.6402962e-03, 3.7556302e-03,
                9.7635266e-04, 3.9882413e-03, 1.7631381e-03, 3.0958296e-03,
                8.8935190e-01, 7.1120202e-03]], dtype=np.float32), 'type': 'Normal'}, 
            {'label': '0', 'prediction': np.array([[9.94274318e-01, 1.90027204e-04, 1.11099485e-04, 1.32014713e-04,
                    6.03598091e-05, 1.53986955e-04, 1.01985340e-03, 5.59141117e-05,
                    2.69676995e-04, 9.24895357e-05, 3.20346764e-04, 2.11196835e-04,
                    4.60514530e-05, 4.90415296e-05, 4.95936874e-05, 8.59268312e-06,
                    2.47093958e-05, 8.97291247e-05, 1.51941110e-03, 4.77592635e-04,
                    2.13305815e-04, 6.64810141e-05, 9.68105087e-05, 1.49815547e-04,
                    3.58933794e-05, 1.17513438e-04, 6.37744306e-05, 1.35416221e-05,
                    7.58659371e-05, 1.10383289e-05]], dtype=np.float32), 'type': 'Normal'}
        ],
        'latex_list': ['0', '(', 'y', '2', '9', '7', '-', '0', '.', '4', '+', '2', '.', '0'],
        'latex_string': '0(y297-0.4+2.0',
        'lstring': '0(y297-0.4+2.0'
    }

    try:
        cg = CheckGrammar()
        cg.check(latex_data3)
    except (GrammarError, SintaticError, LexicalError) as e:
        print('[example.py] Exception: ', e.data)
        print('[example.py] Exception: ', e.valor)

        print(e.data['pure_errors'])
        print(e.data['error'])
        print(e.data['errors_history'])
