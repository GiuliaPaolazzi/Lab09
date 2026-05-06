import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        distanza_x = self._view._txt_distanza.value
        try:
            x_float = float(distanza_x)
        except ValueError:
            self._view.create_allert("Inserire valore numerico per la distanza")
            return
        #eseguiamo la creazione del grafo
        self._model.crea_grafo(x_float)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"Vertici: {self._model.get_num_nodes()}"))
        self._view.txt_result.controls.append(ft.Text(f"Archi: {self._model.get_num_edges()}"))
        for u, v, data in self._model.get_edges_details():
            self._view.txt_result.controls.append(
                ft.Text(f"{u['IATA_CODE']} -> {v['IATA_CODE']} - Distanza media: {data['weight']:.2f}")
            )
        self._view.update_page()
