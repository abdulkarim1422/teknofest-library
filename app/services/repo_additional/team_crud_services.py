from app.repositories import team_crud
from app.repositories import competition_crud
from app.services.repo_additional import competition_crud_services
from app.models.team import Team
from app.models.competition import Report_File

def get_teams_by_competition_en_name(name: str):
    competition_crud_class = competition_crud.CompetitionCRUD()
    competition_obj = competition_crud_class.get_competition_by_en_name(name)
    if competition_obj is None:
        return None
    return team_crud.TeamCRUD.get_teams_by_competition_id(competition_obj.id)

def update_or_create_team(
    name,
    members_list,
    description,
    institution_name,
    comp_name,
    year,
    report_file_path,
    intro_file_path,
    team_link,
    status
):
    print(f"""
          received team info:
            name: {name}
            members_list: {members_list}
            description: {description}
            institution_name: {institution_name}
            comp_name: {comp_name}
            year: {year}
            report_file_path: {report_file_path}
            intro_file_path: {intro_file_path}
            team_link: {team_link}
            status: {status}
        """)
    try:
        competition_obj = competition_crud_services.get_competition_obj_via_any_name(comp_name)
        if competition_obj:
            competition_id = competition_obj.id
        team_crud_class = team_crud.TeamCRUD()
        db_team = team_crud_class.get_team_by_name_and_year(name=name, year=int(year))
        if db_team is None: # create new team
            db_team = Team(
                name=name,
                members_list=members_list,
                description=description,
                institution_name=institution_name,
                competition_id=competition_id,
                year=year,
                intro_file_path=intro_file_path,
                team_link=team_link,
                status=status
            )
            team_crud_class.create_team(db_team)

        else: # update existing team
            db_team.members_list = members_list
            db_team.description = description
            db_team.institution_name = institution_name
            db_team.competition_id = competition_id
            db_team.year = year
            db_team.intro_file_path = intro_file_path
            db_team.team_link = team_link
            db_team.status = status

            team_crud.TeamCRUD.update_team(db_team.id, db_team)

        
        if report_file_path is not None:
            report_file = Report_File(
                competition_id=competition_id,
                team_id=db_team.id,
                year=year,
                file_path=report_file_path,
                rank=status
            )
            team_crud.ReportFileCRUD.create_report_file(report_file)

        return db_team
    except Exception as e:
        print(f"Error while updating or creating team: {e}")
        return None