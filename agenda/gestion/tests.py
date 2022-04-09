from rest_framework.test import APITestCase

class EtiquetasTestCase(APITestCase):
    def test_crear_etiqueta_sucess(self):
        request=self.client.post('/gestion/etiquetas',data={'nombre':'Frontend'})
        print(request.data)
        self.assertEqual(request.status_code,201)


        def test_listar_Etiquetas_failesdd(self):
            request=self.client.get('/gestion/etiquetas')
            print(request.data)