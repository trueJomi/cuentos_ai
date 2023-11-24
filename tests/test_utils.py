from domain.utils.transform import concat_list
from tests.static.data import prueba_service_3_return

def test_concat_list():
    data=prueba_service_3_return()
    assert  concat_list(data,[0,1]) == [
        "Había una vez una niña llamada Caperucita Roja que vivía en una pequeña casa en el bosque. Caperucita Roja era una niña muy curiosa y siempre estaba ansiosa por explorar el mundo que la rodeaba. Un día, su madre llamó a Caperucita Roja y le dijo: \"Querida, tu abuelita está enferma y me gustaría que llevaras esta cesta de comida a su casa\". Caperucita Roja se emocionó mucho y prometió a su madre que llevaría la comida a su abuelita sin demora.",
        "Caperucita Roja se puso su capa roja favorita y comenzó a caminar por el bosque hacia la casa de su abuelita. Mientras caminaba, Caperucita Roja se encontró con un lobo que parecía muy hambriento. El lobo le preguntó a Caperucita Roja adónde iba con tanta prisa, y ella le contó sobre su abuelita enferma y la comida que llevaba para ella. El lobo, en lugar de atacarla, le dijo que conocía un atajo que la llevaría rápidamente a la casa de su abuelita. Al principio, Caperucita Roja estaba un poco asustada, pero el lobo parecía amigable y decidió confiar en él.",
    ]