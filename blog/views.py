from datetime import date

from django.shortcuts import render


all_skills = [
    {
        "slug": "django-programming",
        "image": "Django.png",
        "author": "ner",
        "date": date(2024, 6, 11),
        "title": "Django",
        "excerpt": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It\’s free and open source.",
        "content": """
        Django was created in the autumn of 2003, when the web programmers at the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications. Jacob Kaplan-Moss was hired early in Django\'s development shortly before Simon Willison\'s internship ended. It was released publicly under a BSD license in July 2005. The framework was named after guitarist Django Reinhardt. Adrian Holovaty is a Romani jazz guitar player inspired in part by Reinhardt\'s music.[18]In June 2008, it was announced that a newly formed Django Software Foundation (DSF) would maintain Django in the future
        """
    },
    {
        "slug": "php-programming",
        "image": "php.png",
        "author": "ner",
        "date": date(2024, 6, 11),
        "title": "PHP",
        "excerpt": "PHP code is executed on the server. PHP: Hypertext Preprocessor.",
        "content": """
        PHP is a general-purpose scripting language geared towards web development. It was originally created by Danish-Canadian programmer Rasmus Lerdorf in 1993 and released in 1995. The PHP reference implementation is now produced by the PHP Group. PHP was originally an abbreviation of Personal Home Page, but it now stands for the recursive initialism PHP: Hypertext Preprocessor.
        
        PHP code is usually processed on a web server by a PHP interpreter implemented as a module, a daemon or a Common Gateway Interface (CGI) executable. On a web server, the result of the interpreted and executed PHP code—which may be any type of data, such as generated HTML or binary image data—would form the whole or part of an HTTP response. Various web template systems, web content management systems, and web frameworks exist that can be employed to orchestrate or facilitate the generation of that response. Additionally, PHP can be used for many programming tasks outside the web context, such as standalone graphical applications and drone control.[16] PHP code can also be directly executed from the command line.
        """
    },
    {
        "slug": "delphi-programming",
        "image": "delphi.png",
        "author": "ner",
        "date": date(2024, 6, 11),
        "title": "Delphi",
        "excerpt": "Delphi a general-purpose programming language and a software product that uses the Delphi dialect of the Object Pascal programming language.",
        "content": """
        Delphi is a general-purpose programming language and a software product that uses the Delphi dialect of the Object Pascal programming language and provides an integrated development environment (IDE) for rapid application development of desktop, mobile, web, and console software, currently developed and maintained by Embarcadero Technologies. 
        Delphi's compilers generate native code for Microsoft Windows, macOS, iOS, Android and Linux (x64).
        
        Delphi includes a code editor, a visual designer, an integrated debugger, a source code control component, and support for third-party plugins. The code editor features Code Insight (code completion), Error Insight (real-time error-checking), and refactoring. The visual forms designer has the option of using either the Visual Component Library (VCL) for pure Windows development or the FireMonkey (FMX) framework for cross-platform development. Database support is a key feature and is provided by FireDAC (Database Access Components). Delphi is known for its fast compilation speed, native code, and developer productivity.
        """
    },
    {
        "slug": "csharp-programming",
        "image": "csharp.png",
        "author": "ner",
        "date": date(2024, 6, 11),
        "title": "C#.Net",
        "excerpt": "C# is a modern, innovative, open-source, cross-platform object-oriented programming.",
        "content": """
        C# is a modern, innovative, open-source, cross-platform object-oriented programming language and one of the top 5 programming languages on GitHub. 
        
        Do you have experience with JavaScript, Java, or C++? You'll find C# instantly familiar, and you'll enjoy its evolving features including type safety, generics, pattern matching, async, records, and more. 
        
        We hope you'll fall in love with C# from the very first keystroke.
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.



def starting_page(request):
    sorted_skills = sorted(all_skills, key=get_date)
    latest_skills = sorted_skills[-3:]
    return render(request, "blog/index.html", {
        "skills": latest_skills
    })


def posts(request):
    return render(request, "blog/all-skills.html", {
        "skills": all_skills
    })


def post_details(request, slug):
    indetified_skill = next(skill for skill in all_skills if skill['slug'] == slug)
    return render(request, "blog/skill-detail.html", {
        "skill" : indetified_skill
    })
