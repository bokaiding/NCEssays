"""NCEA Marking Rubrics for various achievement standards."""

MARKING_RUBRICS = {
    # English Level 1 - Unfamiliar Texts
    "AS90858": {
        "name": "Unfamiliar Text",
        "subject": "english",
        "level": 1,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Identifies and explains language features with some understanding of meaning",
                "Supports points with evidence from the text",
                "Shows basic understanding of writer's purpose"
            ],
            "merit": [
                "Analyses language features with in-depth understanding",
                "Justifies interpretations with well-selected evidence",
                "Explains how language features create effects"
            ],
            "excellence": [
                "Demonstrates perceptive understanding of text",
                "Provides comprehensive analysis of language features",
                "Makes insightful connections between ideas",
                "Evaluates effectiveness of writer's choices"
            ]
        }
    },
    
    # English Level 2 - Unfamiliar Texts
    "AS91107": {
        "name": "Respond critically to specified aspect(s) of studied written text(s), supported by evidence",
        "subject": "english",
        "level": 2,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Develops a response using supporting evidence",
                "Explains specified aspect(s) of the text"
            ],
            "merit": [
                "Develops a reasoned response using integrated evidence",
                "Analyses specified aspect(s) of the text"
            ],
            "excellence": [
                "Develops a convincing response using perceptively selected evidence",
                "Evaluates specified aspect(s) of the text"
            ]
        }
    },
    
    # English Level 3 - Unfamiliar Texts
    "AS91472": {
        "name": "Respond critically to significant aspects of visual and/or oral texts through close reading, supported by evidence",
        "subject": "english",
        "level": 3,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Develops a response using supporting evidence",
                "Explains significant aspects of the text"
            ],
            "merit": [
                "Develops a reasoned response using integrated evidence",
                "Analyses significant aspects of the text"
            ],
            "excellence": [
                "Develops a convincing response using perceptively selected evidence",
                "Evaluates significant aspects of the text"
            ]
        }
    },
    
    # History Level 1
    "AS91003": {
        "name": "Describe the relationship between historical perspectives and contexts",
        "subject": "history",
        "level": 1,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Describes historical perspectives",
                "Describes historical contexts"
            ],
            "merit": [
                "Explains the relationship between perspectives and contexts",
                "Uses historical evidence to support explanations"
            ],
            "excellence": [
                "Analyses the relationship between perspectives and contexts",
                "Evaluates the significance of contextual factors"
            ]
        }
    },
    
    # Digital Technologies Level 1
    "AS91896": {
        "name": "Demonstrate understanding of algorithms",
        "subject": "digital_technologies",
        "level": 1,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Describes an algorithm",
                "Explains how the algorithm solves a problem"
            ],
            "merit": [
                "Analyses the algorithm's efficiency",
                "Compares alternative approaches"
            ],
            "excellence": [
                "Evaluates the algorithm's effectiveness",
                "Justifies design decisions with reference to stakeholders"
            ]
        }
    },
    
    # Digital Technologies Level 2
    "AS91897": {
        "name": "Use advanced processes to develop an outcome",
        "subject": "digital_technologies",
        "level": 2,
        "criteria": {
            "not_achieved": "Does not meet Achieved criteria",
            "achieved": [
                "Uses processes to develop an outcome",
                "Documents development process"
            ],
            "merit": [
                "Uses effective processes systematically",
                "Justifies decisions made during development"
            ],
            "excellence": [
                "Uses sophisticated processes efficiently",
                "Critically evaluates and refines outcomes"
            ]
        }
    }
}


def get_rubric(standard_code: str) -> dict:
    """Get marking rubric for a specific standard."""
    return MARKING_RUBRICS.get(standard_code, {})


def format_rubric_for_prompt(standard_code: str) -> str:
    """Format rubric as a prompt-ready string."""
    rubric = get_rubric(standard_code)
    if not rubric:
        return "No specific rubric available. Use general NCEA marking principles."
    
    formatted = f"Achievement Standard: {rubric['name']} (Level {rubric['level']})\n\n"
    formatted += "MARKING CRITERIA:\n\n"
    
    formatted += "Achieved:\n"
    for criterion in rubric['criteria']['achieved']:
        formatted += f"- {criterion}\n"
    
    formatted += "\nMerit:\n"
    for criterion in rubric['criteria']['merit']:
        formatted += f"- {criterion}\n"
    
    formatted += "\nExcellence:\n"
    for criterion in rubric['criteria']['excellence']:
        formatted += f"- {criterion}\n"
    
    return formatted
