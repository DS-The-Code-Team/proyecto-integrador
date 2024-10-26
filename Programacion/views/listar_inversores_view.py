from dao.inversor_dao import InversorDAO

def listar_inversores_view():
    dao = InversorDAO()
    inversores = dao.get_all()
    for inversor in inversores:
        print(inversor)