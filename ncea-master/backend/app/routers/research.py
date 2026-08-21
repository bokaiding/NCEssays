"""API Router for research and search endpoints."""

from fastapi import APIRouter, HTTPException
from typing import Optional, List
import httpx

from ..core.security import limiter

router = APIRouter(prefix="/api/research", tags=["research"])


@router.get("/search")
@limiter.limit("20/minute")
async def search_wikipedia(
    query: str,
    limit: int = 5
):
    """Search Wikipedia for contextual information."""
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://en.wikipedia.org/w/api.php",
                params={
                    "action": "query",
                    "list": "search",
                    "srsearch": query,
                    "format": "json",
                    "srlimit": limit
                },
                timeout=10.0
            )
            response.raise_for_status()
            
            data = response.json()
            results = data.get("query", {}).get("search", [])
            
            return {
                "results": [
                    {
                        "title": r["title"],
                        "snippet": r["snippet"],
                        "url": f"https://en.wikipedia.org/wiki/{r['title'].replace(' ', '_')}"
                    }
                    for r in results
                ]
            }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@router.get("/summary/{title}")
async def get_wikipedia_summary(title: str):
    """Get Wikipedia page summary for a topic."""
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://en.wikipedia.org/w/api.php",
                params={
                    "action": "query",
                    "prop": "extracts|info",
                    "inprop": "url",
                    "titles": title,
                    "format": "json",
                    "exintro": True,
                    "explaintext": True
                },
                timeout=10.0
            )
            response.raise_for_status()
            
            data = response.json()
            pages = data.get("query", {}).get("pages", {})
            
            # Get the first (and only) page
            page_id = next(iter(pages.keys()))
            page = pages[page_id]
            
            if page_id == "-1":
                raise HTTPException(status_code=404, detail="Page not found")
            
            return {
                "title": page["title"],
                "summary": page.get("extract", ""),
                "url": page.get("fullurl", "")
            }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Summary retrieval failed: {str(e)}")


@router.get("/ncea-resources")
async def get_ncea_resources(
    subject: Optional[str] = None,
    level: Optional[int] = None
):
    """Get curated NCEA resources and past papers."""
    
    # This would typically query a database of NCEA resources
    # For now, return a static structure that would be populated
    
    resources = {
        "english": {
            "level_1": {
                "standards": ["AS90858", "AS90849", "AS90856"],
                "past_papers": [],
                "exemplars": []
            },
            "level_2": {
                "standards": ["AS91107", "AS91098", "AS91103"],
                "past_papers": [],
                "exemplars": []
            },
            "level_3": {
                "standards": ["AS91472", "AS91476", "AS91478"],
                "past_papers": [],
                "exemplars": []
            }
        },
        "history": {
            "level_1": {
                "standards": ["AS91003", "AS91001", "AS91002"],
                "past_papers": [],
                "exemplars": []
            },
            "level_2": {
                "standards": ["AS91233", "AS91229", "AS91231"],
                "past_papers": [],
                "exemplars": []
            },
            "level_3": {
                "standards": ["AS91434", "AS91432", "AS91433"],
                "past_papers": [],
                "exemplars": []
            }
        },
        "digital_technologies": {
            "level_1": {
                "standards": ["AS91896", "AS91897", "AS91898"],
                "past_papers": [],
                "exemplars": []
            },
            "level_2": {
                "standards": ["AS91897", "AS91898", "AS91899"],
                "past_papers": [],
                "exemplars": []
            },
            "level_3": {
                "standards": ["AS91906", "AS91907", "AS91908"],
                "past_papers": [],
                "exemplars": []
            }
        }
    }
    
    if subject and level:
        key = f"level_{level}"
        return resources.get(subject, {}).get(key, {"error": "No resources found"})
    elif subject:
        return resources.get(subject, {"error": "Subject not found"})
    
    return resources
