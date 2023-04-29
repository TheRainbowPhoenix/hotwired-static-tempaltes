from .viteLoader import vite_asset  # , vite_hmr_client
import typing
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseSettings

import mimetypes
mimetypes.init()

mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('image/svg+xml', '.svg')

# import fastapi_vite


class Settings(BaseSettings):
    site_name: str = "GoodbyeJob"
    site_url: str = "http://127.0.0.1:8080"  # "https://goodbye.konshin.ml"


settings = Settings()
app = FastAPI(settings=settings)


def app_context(request: Request) -> typing.Dict[str, typing.Any]:
    return {'app': request.app}


def vite_hmr_client():
    return ""


# def vite_asset(file):
#     return ""


templates = Jinja2Templates(directory="templates",
                            context_processors=[app_context])
templates.env.globals['vite_hmr_client'] = vite_hmr_client
templates.env.globals['vite_asset'] = vite_asset

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/fr-fr/emplois/{id}", response_class=HTMLResponse)
async def job_detail(request: Request, id: int):
    return templates.TemplateResponse("job_detail.html", {
        "request": request,
        "data": data,
        "dataLayer": {
            "todo": "dataLayer"
        },
        "seo": {
            "title": "#Entreprise# Recrutement - Candidature Rapide et Facile | GoodbyeWork",
            "description": "Consultez les Dernières Offres d'Emploi de #Entreprise# sur GoodbyeWork. ✓ Postulez en ligne dès Maintenant ✓ Candidature Simple & Rapide !",
            "slug": f"/fr-fr/entreprises/{entreprise_name}-{id}",
            "og_image": "goodbyework/img/seo/defaultGoodbyework.png",
            "ld_breadcrumb": [
                {
                    "@type": "ListItem",
                    "position": 0,
                    "item": {
                        "@id": f"{SITE}/fr-fr/",
                        "name": "Accueil"
                    }
                },
                {
                    "@type": "ListItem",
                    "position": 1,
                    "item": {
                        "@id": f"{settings.site_url}/fr-fr/emploi.html",
                        "name": "Emploi"
                    }
                },
                {
                    "@type": "ListItem",
                    position: 2,
                    item: {
                        "@id":
                        f"{settings.site_url}fr-fr/emploi/region_name.html",
                        name: "Emploi Region",
                    },
                },
                {
                    "@type": "ListItem",
                    position: 3,
                    item: {
                        "@id":
                        f"{settings.site_url}fr-fr/emploi/departement_name-00.html",
                        name: "Emploi Departement",
                    },
                },
                {
                    "@type": "ListItem",
                    position: 4,
                    item: {
                        "@id":
                        f"{settings.site_url}fr-fr/emploi/ville_name-00000.html",
                        name: "Emploi Ville",
                    },
                },
                {
                    "@type": "ListItem",
                    position: 5,
                    item: {
                        "@id":
                        f"{settings.site_url}fr-fr/emploi/metier_name-ville_name-00000.html",
                        name: "Emploi Metier",
                    },
                },
                {
                    "@type": "ListItem",
                    position: 6,
                    item: {name: "Metier Name H/F"},
                },
            ],
            "ld_job_posting": {
                "@context": "https://schema.org",
                "@type": "JobPosting",
                "TODO": "TODO"
            }
        }
    })


@ app.get("/fr-fr/entreprises/{entreprise_name}-{id}", response_class=HTMLResponse)
async def page(request: Request, entreprise_name: str, id: int):
    data = {
        "entreprise": id,
        "name": entreprise_name
    }
    return templates.TemplateResponse("entreprise.html", {
        "request": request,
        "data": data,
        "dataLayer": {
            "todo": "dataLayer"
        },
        "seo": {
            "title": f"{entreprise_name.title()} Recrutement - Candidature Rapide et Facile | GoodbyeWork",
            "description": f"Consultez les Dernières Offres d'Emploi de {entreprise_name.title()} sur GoodbyeWork. ✓ Postulez en ligne dès Maintenant ✓ Candidature Simple & Rapide !",
            "slug": f"/fr-fr/entreprises/{entreprise_name}-{id}",
            "og_image": "goodbyework/img/seo/defaultGoodbyework.png",
            "ld_breadcrumb": [
                {
                    "@type": "ListItem",
                    "position": 0,
                    "item": {
                        "@id": f"{settings.site_url}/fr-fr/",
                        "name": "Accueil"
                    }
                },
                {
                    "@type": "ListItem",
                    "position": 1,
                    "item": {
                        "@id": f"{settings.site_url}/fr-fr/entreprise.html",
                        "name": "Entreprise"
                    }
                },
                {"@type": "ListItem", "position": 2,
                    "item": {"name": f"{entreprise_name.title()}"}}
            ]
        }
    })
