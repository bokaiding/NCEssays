"""NCEA English Marking Rubrics for all achievement standards across Levels 1-3 and Scholarship."""

MARKING_RUBRICS = {
    # ==================== LEVEL 1 ENGLISH ====================
    # AS90858 - Unfamiliar Texts (Level 1)
    "AS90858": {
        "name": "Unfamiliar Text",
        "subject": "english",
        "level": 1,
        "credits": 4,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Identifies and explains language features with some understanding of meaning",
                "Supports points with evidence from the text",
                "Shows basic understanding of writer's purpose and audience"
            ],
            "merit": [
                "Analyses language features with in-depth understanding of meaning",
                "Justifies interpretations with well-selected evidence",
                "Explains how language features create specific effects"
            ],
            "excellence": [
                "Demonstrates perceptive understanding of text and its implications",
                "Provides comprehensive analysis of language features and their effects",
                "Makes insightful connections between ideas and themes",
                "Evaluates effectiveness of writer's choices critically"
            ]
        }
    },
    
    # AS90856 - Writing (Level 1)
    "AS90856": {
        "name": "Write selected texts",
        "subject": "english",
        "level": 1,
        "credits": 6,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Creates texts that show understanding of purpose and audience",
                "Uses language features appropriate to the text type",
                "Organises ideas with some coherence"
            ],
            "merit": [
                "Creates texts that develop ideas with depth",
                "Uses language features effectively for intended purpose",
                "Structures texts coherently with logical sequencing"
            ],
            "excellence": [
                "Creates sophisticated texts with perceptive understanding",
                "Uses language features with precision and flair",
                "Crafts texts with seamless structure and compelling flow"
            ]
        }
    },
    
    # AS90857 - Oral Presentation (Level 1)
    "AS90857": {
        "name": "Deliver an oral presentation",
        "subject": "english",
        "level": 1,
        "credits": 4,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Presents information clearly with some engagement",
                "Uses verbal and non-verbal features appropriately"
            ],
            "merit": [
                "Presents with sustained engagement and clarity",
                "Uses verbal and non-verbal features effectively"
            ],
            "excellence": [
                "Presents with compelling engagement and sophistication",
                "Uses verbal and non-verbal features with polish and impact"
            ]
        }
    },
    
    # ==================== LEVEL 2 ENGLISH ====================
    # AS91107 - Written Texts (Level 2)
    "AS91107": {
        "name": "Respond critically to specified aspect(s) of studied written text(s), supported by evidence",
        "subject": "english",
        "level": 2,
        "credits": 4,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Develops a response using supporting evidence from the text",
                "Explains specified aspect(s) such as character, theme, or setting"
            ],
            "merit": [
                "Develops a reasoned response using integrated evidence",
                "Analyses specified aspect(s) showing deeper understanding"
            ],
            "excellence": [
                "Develops a convincing response using perceptively selected evidence",
                "Evaluates specified aspect(s) with critical insight"
            ]
        }
    },
    
    # AS91108 - Unfamiliar Texts (Level 2)
    "AS91108": {
        "name": "Respond critically to aspects of unfamiliar written text(s), supported by evidence",
        "subject": "english",
        "level": 2,
        "credits": 4,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Develops a response using supporting evidence from the text",
                "Explains aspects such as language features, purpose, or audience"
            ],
            "merit": [
                "Develops a reasoned response using integrated evidence",
                "Analyses aspects showing understanding of writer's craft"
            ],
            "excellence": [
                "Develops a convincing response using perceptively selected evidence",
                "Evaluates aspects with critical insight into writer's choices"
            ]
        }
    },
    
    # AS91106 - Oral Presentation (Level 2)
    "AS91106": {
        "name": "Form and deliver an oral presentation",
        "subject": "english",
        "level": 2,
        "credits": 4,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Forms and delivers a presentation with clear purpose",
                "Uses verbal and non-verbal features appropriately"
            ],
            "merit": [
                "Forms and delivers a presentation with sustained engagement",
                "Uses verbal and non-verbal features effectively"
            ],
            "excellence": [
                "Forms and delivers a presentation with compelling impact",
                "Uses verbal and non-verbal features with sophistication"
            ]
        }
    },
    
    # AS91105 - Writing (Level 2)
    "AS91105": {
        "name": "Write a selection of crafted and controlled writing",
        "subject": "english",
        "level": 2,
        "credits": 6,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Creates texts showing control of language",
                "Demonstrates awareness of purpose and audience"
            ],
            "merit": [
                "Creates crafted texts with effective language use",
                "Shows deliberate crafting for purpose and audience"
            ],
            "excellence": [
                "Creates sophisticated texts with precise control",
                "Demonstrates perceptive crafting with distinctive voice"
            ]
        }
    },
    
    # ==================== LEVEL 3 ENGLISH ====================
    # AS91472 - Visual/Oral Texts (Level 3)
    "AS91472": {
        "name": "Respond critically to significant aspects of visual and/or oral texts through close reading, supported by evidence",
        "subject": "english",
        "level": 3,
        "credits": 4,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Develops a response using supporting evidence",
                "Explains significant aspects of the text"
            ],
            "merit": [
                "Develops a reasoned response using integrated evidence",
                "Analyses significant aspects showing deeper understanding"
            ],
            "excellence": [
                "Develops a convincing response using perceptively selected evidence",
                "Evaluates significant aspects with critical insight"
            ]
        }
    },
    
    # AS91473 - Written Texts (Level 3)
    "AS91473": {
        "name": "Respond critically to specified aspect(s) of studied written text(s), supported by evidence",
        "subject": "english",
        "level": 3,
        "credits": 4,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Develops a response using supporting evidence",
                "Explains specified aspect(s) of the text"
            ],
            "merit": [
                "Develops a reasoned response using integrated evidence",
                "Analyses specified aspect(s) with depth"
            ],
            "excellence": [
                "Develops a convincing response using perceptively selected evidence",
                "Evaluates specified aspect(s) with sophisticated insight"
            ]
        }
    },
    
    # AS91476 - Create a fluent text (Level 3)
    "AS91476": {
        "name": "Create a fluent text",
        "subject": "english",
        "level": 3,
        "credits": 6,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Creates a text that is coherent and fluent",
                "Uses language features appropriately"
            ],
            "merit": [
                "Creates a text with controlled fluency",
                "Uses language features effectively"
            ],
            "excellence": [
                "Creates a text with sophisticated fluency",
                "Uses language features with precision and style"
            ]
        }
    },
    
    # AS91477 - Respond to literature (Level 3)
    "AS91477": {
        "name": "Respond critically to ideas in literary texts, supported by evidence",
        "subject": "english",
        "level": 3,
        "credits": 4,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Develops a response to ideas using evidence",
                "Explains how ideas are presented"
            ],
            "merit": [
                "Develops a reasoned response to ideas",
                "Analyses how ideas shape meaning"
            ],
            "excellence": [
                "Develops a convincing response to ideas",
                "Evaluates the significance of ideas critically"
            ]
        }
    },
    
    # ==================== SCHOLARSHIP ENGLISH ====================
    # Scholarship English - Performance Standard
    "SCHOLARSHIP_ENGLISH": {
        "name": "Scholarship English",
        "subject": "english",
        "level": "scholarship",
        "credits": 0,
        "criteria": {
            "not_achieved": "Does not meet Scholarship criteria",
            "achieved": [
                "Demonstrates competent understanding of complex texts",
                "Constructs coherent responses with supporting evidence",
                "Shows awareness of context and purpose"
            ],
            "merit": [
                "Demonstrates secure understanding with perceptive insights",
                "Constructs well-reasoned arguments with integrated evidence",
                "Analyses relationships between text, context, and meaning"
            ],
            "excellence": [
                "Demonstrates outstanding critical thinking with original insights",
                "Constructs sophisticated, convincing arguments",
                "Evaluates texts with exceptional perceptiveness and depth",
                "Synthesises ideas across texts and contexts masterfully"
            ]
        },
        "scholarship_notes": [
            "Scholarship requires demonstration of high-level critical thinking",
            "Responses must show originality and independence of thought",
            "Integration of multiple texts and perspectives is expected",
            "Writing must be polished, precise, and compelling"
        ]
    }
}


def get_rubric(standard_code: str) -> dict:
    """Get marking rubric for a specific standard."""
    return MARKING_RUBRICS.get(standard_code, {})


def format_rubric_for_prompt(standard_code: str) -> str:
    """Format rubric as a prompt-ready string."""
    rubric = get_rubric(standard_code)
    if not rubric:
        return "No specific rubric available. Use general NCEA English marking principles."
    
    formatted = f"Achievement Standard: {rubric['name']} (Level {rubric['level']})\n"
    formatted += f"Credits: {rubric.get('credits', 'N/A')}\n\n"
    formatted += "MARKING CRITERIA:\n\n"
    
    formatted += "Not Achieved:\n"
    formatted += f"- {rubric['criteria']['not_achieved']}\n\n"
    
    formatted += "Achieved:\n"
    for criterion in rubric['criteria']['achieved']:
        formatted += f"- {criterion}\n"
    
    formatted += "\nMerit:\n"
    for criterion in rubric['criteria']['merit']:
        formatted += f"- {criterion}\n"
    
    formatted += "\nExcellence:\n"
    for criterion in rubric['criteria']['excellence']:
        formatted += f"- {criterion}\n"
    
    # Add scholarship-specific notes if applicable
    if standard_code == "SCHOLARSHIP_ENGLISH" and "scholarship_notes" in rubric:
        formatted += "\n\nSCHOLARSHIP EXPECTATIONS:\n"
        for note in rubric['scholarship_notes']:
            formatted += f"- {note}\n"
    
    return formatted


def get_all_english_standards() -> list:
    """Return list of all English achievement standards."""
    return [
        {"code": code, "name": data["name"], "level": data["level"]}
        for code, data in MARKING_RUBRICS.items()
    ]


def get_standards_by_level(level: str) -> list:
    """Filter standards by level (1, 2, 3, or scholarship)."""
    return [
        {"code": code, "name": data["name"]}
        for code, data in MARKING_RUBRICS.items()
        if data["level"] == level or (level == "scholarship" and data["level"] == "scholarship")
    ]
