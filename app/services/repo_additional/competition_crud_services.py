from app.repositories import competition_crud
from app.services.unify.function import find_original_sentence

def get_competition_application_link_via_en_name(name: str):
    competition_crud_class = competition_crud.CompetitionCRUD()
    competition_obj = competition_crud_class.get_competition_by_en_name(name)
    if competition_obj is None:
        return None
    return competition_obj.application_link

def get_competition_en_name_via_any_name(name: str):
    competition_crud_class = competition_crud.CompetitionCRUD()
    unified_name = find_original_sentence(name)
    competition_obj = competition_crud_class.get_competition_by_en_name(name=unified_name)
    if competition_obj is None:
        competition_obj = competition_crud_class.get_competition_by_tr_name(name=name)
        if competition_obj is None:
            competition_obj = competition_crud_class.get_competition_by_en_name(name=name)
            if competition_obj is None:
                competition_obj = competition_crud_class.get_competition_by_ar_name(name=name)
                if competition_obj is None:
                    return None
    return competition_obj.en_name

def update_or_create_competition(
        image_link,
        tk_number,
        t3kys_number,
        application_link_tr,
        application_link_en,
        application_link_ar,
        tr_name,
        tr_description,
        tr_link,
        en_name,
        en_description,
        en_link,
        ar_name,
        ar_description,
        ar_link,
        year,
        min_member,
        max_member
):
    print(f"""
            received competition info:
            image_link: {image_link}
            tk_number: {tk_number}
            t3kys_number: {t3kys_number}
            application_link_tr: {application_link_tr}
            application_link_en: {application_link_en}
            application_link_ar: {application_link_ar}
            tr_name: {tr_name}
            tr_description: {tr_description}
            tr_link: {tr_link}
            en_name: {en_name}
            en_description: {en_description}
            en_link: {en_link}
            ar_name: {ar_name}
            ar_description: {ar_description}
            ar_link: {ar_link}
            year: {year}
            min_member: {min_member}
            max_member: {max_member}
        """)
    