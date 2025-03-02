from app.repositories import competition_crud

def get_competition_application_link_via_en_name(name: str):
    competition_obj = competition_crud.CompetitionCRUD.get_competition_by_en_name(name)
    if competition_obj is None:
        return None
    return competition_obj.application_link

def get_competition_en_name_via_any_name(name: str):
    competition_obj = competition_crud.CompetitionCRUD.get_competition_by_tr_name(name)
    if competition_obj is None:
        competition_obj = competition_crud.CompetitionCRUD.get_competition_by_en_name(name)
        if competition_obj is None:
            competition_obj = competition_crud.CompetitionCRUD.get_competition_by_ar_name(name)
            if competition_obj is None:
                return None
    return competition_obj.en_name