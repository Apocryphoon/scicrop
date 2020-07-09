from pip._vendor import requests

json = {
    "full_name": "Ricardo Ribeiro Cardoso",
	"email": "ricardo.rc15@hotmail.com",
	"mobile_phone": "(11) 94555-5915",
	"age": 19,
	"home_address": "Rua joão tezza, 48",
	"start_date": 30092000,
	"opportunity_tag": "estágio_dev",
	"past_jobs_experience": "Trabalhei por volta de 6 meses em uma corretora com devesenvolvimento.",
	"degrees": [{
		"institution_name": "BGC Liquidez",
		"begin_date": 13112019,
		"end_date": 452020
	}],
	"programming_skills": ["html5", "css3", "dotnet", "python"],
	"database_skills": ["mysql"],
	"hobbies": ["jogar", "estudar"],
	"why": "Atualmente tenho 19 anos, moro com meus pais e irmão, sou amante do mundo geek e estudante de programação, confesso que não conheço muito de python, porém estou disposto a me desempenhar.",
	"git_url_repositories": "https://github.com/Apocryphoon/scicrop"
}
r = requests.post('https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume', json=json)
print(r.text)
print("================== RESPOSTA POST ===================")
print(r)
print("====================================================")