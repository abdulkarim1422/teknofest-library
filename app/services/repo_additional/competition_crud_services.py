from app.repositories import competition_crud
from app.services.unify.function import find_original_sentence
from app.models.competition import Competition

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
        link,
        image_link,
        tk_number,
        t3kys_number,
        application_link,
        comp_name,
        comp_description,
        comp_link,
        year,
        min_member,
        max_member,
        lang
):
    print(f"""
            received competition info:
            link: {link}
            image_link: {image_link}
            tk_number: {tk_number}
            t3kys_number: {t3kys_number}
            application_link: {application_link}
            comp_name: {comp_name}
            comp_description: {comp_description}
            comp_link: {comp_link}
            year: {year}
            min_member: {min_member}
            max_member: {max_member}]
            lang: {lang}
        """)
    
    if "teknofest.org/tr" in link:
        lang = "tr"
        competition_obj = get_competition_en_name_via_any_name(tr_name)
    elif "teknofest.org/en" in link:
        lang = "en"
        competition_obj = get_competition_en_name_via_any_name(en_name)
    else:
        lang = "ar"
        competition_obj = get_competition_en_name_via_any_name(ar_name)

    if competition_obj:
        competition_id = competition_obj.id
    competition_crud_class = competition_crud.CompetitionCRUD()
    db_competition = competition_crud_class.get_competition(competition_id)

    if db_competition is None:  # create new competition
        db_competition = Competition(
            image_path=image_link,
            tk_number=tk_number,
            t3kys_number=t3kys_number,
            application_link_tr=application_link_tr,
            application_link_en=application_link_en,
            application_link_ar=application_link_ar,
            tr_name=tr_name,
            tr_description=tr_description,
            tr_link=tr_link,
            en_name=en_name,
            en_description=en_description,
            en_link=en_link,
            ar_name=ar_name,
            ar_description=ar_description,
            ar_link=ar_link,
            years=[year],
            min_member=min_member,
            max_member=max_member
        )
        competition_crud_class.create_competition(db_competition)

    else:  # update existing competition
        db_competition.image_path = image_link
        db_competition.tk_number = tk_number
        db_competition.t3kys_number = t3kys_number
        db_competition.application_link_tr = application_link_tr
        db_competition.application_link_en = application_link_en
        db_competition.application_link_ar = application_link_ar
        db_competition.tr_name = tr_name
        db_competition.tr_description = tr_description
        db_competition.tr_link = tr_link
        db_competition.en_name = en_name
        db_competition.en_description = en_description
        db_competition.en_link = en_link
        db_competition.ar_name = ar_name
        db_competition.ar_description = ar_description
        db_competition.ar_link = ar_link
        db_competition.years.append(year)
        db_competition.min_member = min_member
        db_competition.max_member = max_member

        competition_crud_class.update_competition(competition_id, db_competition)

    return db_competition


