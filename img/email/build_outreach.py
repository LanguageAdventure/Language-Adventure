# Builds img/email/outreach-<lang>.html for the Language Adventure outreach email.
# Run from the repo root: python3 img/email/build_outreach.py
B = 'https://languageadventure.github.io/Language-Adventure/img/email/'
S = B + 'sig/'
SIGN = 'https://languageadventure.github.io/Language-Adventure/demo.html'
TRAILER = 'https://www.youtube.com/watch?v=wJoiifm54UY'
ITCH = 'https://language-adventure.itch.io/language-adventure'
STEAM = 'https://store.steampowered.com/app/2204770'
PS = 'margin:0 0 16px;font-family:Nunito,Arial,sans-serif;font-size:16px;line-height:1.6;color:#222'

T = {
 'en': dict(
  subject='Language Adventure – A stop-motion language learning game',
  hi='Hi!',
  p2="I'm Chris, a solo developer at Wonky Games, and I've been making Language Adventure. It's a point-and-click adventure game to help learn English, for beginner and intermediate learners of all ages.",
  p3="You can explore a handmade town that's all filmed in stop motion. Everything is labelled and has descriptions with helpful vocabulary. Click on anything to hear what it is in spoken English, narrated by Adam Buxton.",
  p5a="A free demo is coming to Steam and {itch} for Windows, Mac &amp; Linux on 13 January, but you can play it early by joining the playtest through the form on the website.",
  p5b="Sign-ups are open from now until 26th November. You don't have to actually playtest the game, so feel free to join even if you're just curious!",
  p6="I think it could be a useful tool for your viewers, and I'd love it if you'd give it a try. If you'd like to know anything, feel free to ask.",
  p7="Hope you're having a lovely week!",
  p8="Kind regards,<br>Chris",
  a1='Scenes from Language Adventure', a2='A room in Language Adventure',
  atr='Watch the Language Adventure trailer', alogo='Language Adventure: join the playtest', amail='Email'),
 'fr': dict(
  subject='Language Adventure – un jeu d\'apprentissage des langues en stop motion',
  hi='Salut !',
  p2="Je m'appelle Chris, développeur solo chez Wonky Games, et je crée Language Adventure. C'est un jeu d'aventure point-and-click pour apprendre l'anglais, destiné aux apprenants débutants et intermédiaires de tous âges.",
  p3="Tu peux explorer une ville faite à la main, entièrement filmée en stop motion. Tout est étiqueté et accompagné de descriptions avec du vocabulaire utile. Clique sur n'importe quoi pour entendre ce que c'est en anglais parlé, avec la narration d'Adam Buxton.",
  p5a="Une démo gratuite sortira sur Steam et {itch} pour Windows, Mac et Linux le 13 janvier, mais tu peux y jouer en avant-première en t'inscrivant au playtest via le formulaire sur le site.",
  p5b="Les inscriptions sont ouvertes dès maintenant et jusqu'au 26 novembre. Pas besoin de vraiment tester le jeu : tu peux t'inscrire même par simple curiosité !",
  p6="Je pense que ça pourrait être un outil utile pour tes spectateurs, et j'aimerais beaucoup que tu l'essaies. Si tu veux savoir quoi que ce soit, n'hésite pas à demander.",
  p7="Je te souhaite une très bonne semaine !",
  p8="Bien à toi,<br>Chris",
  a1='Scènes de Language Adventure', a2='Une pièce dans Language Adventure',
  atr='Regarder la bande-annonce de Language Adventure', alogo='Language Adventure : rejoindre le playtest', amail='E-mail'),
 'de': dict(
  subject='Language Adventure – ein Sprachlernspiel in Stop-Motion',
  hi='Hallo!',
  p2="Ich bin Chris, Solo-Entwickler bei Wonky Games, und entwickle gerade Language Adventure. Es ist ein Point-and-Click-Adventure zum Englischlernen für Lernende jeden Alters auf Anfänger- und Mittelstufenniveau.",
  p3="Du kannst eine handgemachte Stadt erkunden, die komplett in Stop-Motion gefilmt ist. Alles ist beschriftet und hat Beschreibungen mit nützlichem Wortschatz. Klick auf irgendetwas, um zu hören, was es ist – auf gesprochenem Englisch, erzählt von Adam Buxton.",
  p5a="Am 13. Januar erscheint eine kostenlose Demo auf Steam und {itch} für Windows, Mac und Linux, aber du kannst sie schon vorher spielen, wenn du dich über das Formular auf der Website für den Playtest anmeldest.",
  p5b="Die Anmeldung ist ab sofort bis zum 26. November möglich. Du musst das Spiel nicht wirklich testen – melde dich gern an, auch wenn du nur neugierig bist!",
  p6="Ich glaube, es könnte ein nützliches Werkzeug für deine Zuschauer sein, und ich würde mich sehr freuen, wenn du es ausprobierst. Wenn du etwas wissen möchtest, frag gern.",
  p7="Ich wünsche dir eine schöne Woche!",
  p8="Viele Grüße<br>Chris",
  a1='Szenen aus Language Adventure', a2='Ein Zimmer in Language Adventure',
  atr='Den Trailer zu Language Adventure ansehen', alogo='Language Adventure: beim Playtest mitmachen', amail='E-Mail'),
 'es': dict(
  subject='Language Adventure – un juego para aprender idiomas en stop motion',
  hi='¡Hola!',
  p2="Soy Chris, desarrollador en solitario en Wonky Games, y estoy creando Language Adventure. Es un juego de aventuras point-and-click para aprender inglés, para estudiantes de nivel principiante e intermedio de todas las edades.",
  p3="Puedes explorar un pueblo hecho a mano y filmado por completo en stop motion. Todo está etiquetado y tiene descripciones con vocabulario útil. Haz clic en cualquier cosa para oír qué es en inglés hablado, con la narración de Adam Buxton.",
  p5a="El 13 de enero saldrá una demo gratuita en Steam e {itch} para Windows, Mac y Linux, pero puedes jugarla antes apuntándote al playtest con el formulario de la web.",
  p5b="Las inscripciones están abiertas desde ya hasta el 26 de noviembre. No hace falta que pruebes el juego de verdad: ¡apúntate aunque solo sea por curiosidad!",
  p6="Creo que podría ser una herramienta útil para tus espectadores y me encantaría que lo probaras. Si quieres saber algo, no dudes en preguntar.",
  p7="¡Que tengas una semana estupenda!",
  p8="Un saludo,<br>Chris",
  a1='Escenas de Language Adventure', a2='Una habitación en Language Adventure',
  atr='Ver el tráiler de Language Adventure', alogo='Language Adventure: únete al playtest', amail='Correo'),
 'it': dict(
  subject='Language Adventure – un gioco per imparare le lingue in stop motion',
  hi='Ciao!',
  p2="Sono Chris, sviluppo giochi da solo con Wonky Games, e sto realizzando Language Adventure. È un'avventura punta e clicca per imparare l'inglese, pensata per studenti di livello principiante e intermedio di tutte le età.",
  p3="Puoi esplorare una città fatta a mano e girata interamente in stop motion. Ogni cosa ha un'etichetta e una descrizione con vocaboli utili. Clicca su qualsiasi cosa per sentire cos'è in inglese parlato, con la voce narrante di Adam Buxton.",
  p5a="Il 13 gennaio uscirà una demo gratuita su Steam e {itch} per Windows, Mac e Linux, ma puoi giocarci in anteprima iscrivendoti al playtest tramite il modulo sul sito.",
  p5b="Le iscrizioni sono aperte da subito fino al 26 novembre. Non devi per forza testare il gioco: iscriviti pure anche solo per curiosità!",
  p6="Penso che potrebbe essere uno strumento utile per i tuoi spettatori e mi farebbe davvero piacere se lo provassi. Se vuoi sapere qualcosa, chiedi pure.",
  p7="Ti auguro una bellissima settimana!",
  p8="Un caro saluto,<br>Chris",
  a1='Scene da Language Adventure', a2='Una stanza in Language Adventure',
  atr='Guarda il trailer di Language Adventure', alogo='Language Adventure: partecipa al playtest', amail='Email'),
 'pt': dict(
  subject='Language Adventure – um jogo para aprender línguas em stop motion',
  hi='Olá!',
  p2="Sou o Chris, um programador a solo da Wonky Games, e tenho estado a criar o Language Adventure. É um jogo de aventura point-and-click para aprender inglês, para alunos de nível principiante e intermédio de todas as idades.",
  p3="Podes explorar uma cidade feita à mão e filmada inteiramente em stop motion. Tudo tem uma etiqueta e uma descrição com vocabulário útil. Clica em qualquer coisa para ouvires o que é em inglês falado, com narração de Adam Buxton.",
  p5a="A 13 de janeiro vai sair uma demo gratuita no Steam e no {itch} para Windows, Mac e Linux, mas podes jogá-la mais cedo inscrevendo-te no playtest através do formulário do site.",
  p5b="As inscrições estão abertas a partir de agora e até 26 de novembro. Não precisas de testar o jogo a sério; podes inscrever-te mesmo que seja só por curiosidade!",
  p6="Acho que pode ser uma ferramenta útil para os teus espectadores e adorava que o experimentasses. Se quiseres saber alguma coisa, não hesites em perguntar.",
  p7="Espero que estejas a ter uma ótima semana!",
  p8="Um abraço,<br>Chris",
  a1='Cenas do Language Adventure', a2='Uma divisão no Language Adventure',
  atr='Ver o trailer do Language Adventure', alogo='Language Adventure: junta-te ao playtest', amail='Email'),
}


def esc(t):
    return t.replace("'", '&#39;')


def build(t):
    P = lambda x: f'<p style="{PS}">{x}</p>'
    td = lambda inner: f'<tr><td style="padding:0 8px">\n{inner}\n</td></tr>'
    framed = lambda src, alt: f'<img src="{src}" alt="{alt}" width="360" style="width:360px;max-width:100%;height:auto;border:6px solid #fff;border-radius:4px;display:block;margin:0 auto">'
    big = lambda h, n, l: f'<a href="{h}" target="_blank" title="{l}" style="text-decoration:none;display:inline-block;margin:0 10px"><img src="{S}{n}.png" alt="{l}" width="64" height="64" style="width:64px;height:64px;border:0;display:inline-block"></a>'
    small = lambda h, n, l: f'<a href="{h}" target="_blank" title="{l}" style="text-decoration:none;display:inline-block;margin:0 4px"><img src="{S}{n}.png" alt="{l}" width="48" height="48" style="width:48px;height:48px;border:0;display:inline-block;vertical-align:middle"></a>'
    itch = f'<a href="{ITCH}" target="_blank" style="color:#222">itch.io</a>'
    mail = f'<p style="margin:0 0 8px"><a href="mailto:gameswonky@gmail.com" title="{t["amail"]}" style="text-decoration:none;display:inline-block"><img src="{S}letter.png" alt="{t["amail"]}" width="60" height="60" style="width:60px;height:60px;border:0;display:inline-block"></a></p>'
    social = [('https://www.patreon.com/c/LanguageAdventureEnglish', 'patreon', 'Patreon'), ('https://ko-fi.com/languageadventure', 'kofi', 'Ko-fi'),
              ('https://www.instagram.com/wonky_games/', 'instagram', 'Instagram'), ('https://bsky.app/profile/languageadventure.bsky.social', 'bluesky', 'Bluesky'),
              ('https://www.reddit.com/r/LanguageAdventure/', 'reddit', 'Reddit')]
    rows = [
        td(P(t['hi']) + '\n' + P(esc(t['p2']))),
        f'<tr><td align="center" style="padding:4px 8px 20px">{framed(B + "slideshow1-360.gif", t["a1"])}</td></tr>',
        td(P(esc(t['p3']))),
        f'<tr><td align="center" style="padding:4px 8px 20px">{framed(B + "slideshow2-360.gif", t["a2"])}</td></tr>',
        f'<tr><td align="center" style="padding:4px 8px 20px"><a href="{TRAILER}" target="_blank" title="{t["atr"]}">{framed(B + "trailer-thumb.jpg", t["atr"])}</a></td></tr>',
        f'<tr><td align="center" style="padding:0 8px 14px">{big(STEAM, "steam", "Steam")}{big(ITCH, "itch", "itch.io")}</td></tr>',
        td(P(esc(t['p5a']).format(itch=itch))),
        f'<tr><td align="center" style="padding:0 8px 12px"><a href="{SIGN}" target="_blank" title="{t["alogo"]}"><img src="{S}logo.png" alt="{t["alogo"]}" width="240" style="width:240px;height:auto;border:0;display:inline-block"></a><br><a href="{SIGN}" target="_blank" style="font-family:Nunito,Arial,sans-serif;font-size:16px;font-weight:bold;color:#222">LanguageAdventure.info</a></td></tr>',
        td('\n'.join([P(esc(t['p5b'])), P(esc(t['p6'])), P(esc(t['p7'])), P(t['p8']), mail])),
        f'<tr><td align="center" style="padding:16px 0 10px;white-space:nowrap">{"".join(small(*s) for s in social)}</td></tr>',
    ]
    return ('<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFCC00" style="width:100%;background-color:#FFCC00"><tbody><tr><td align="center" bgcolor="#FFCC00" style="background-color:#FFCC00;padding:28px 12px">\n'
            '<table role="presentation" width="560" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:560px"><tbody>\n'
            + '\n'.join(rows) + '\n</tbody></table>\n</td></tr></tbody></table>')


if __name__ == '__main__':
    import json
    for lang, t in T.items():
        open(f'img/email/outreach-{lang}.html', 'w', encoding='utf-8').write(build(t))
    json.dump({l: t['subject'] for l, t in T.items()}, open('img/email/subjects.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('built', list(T))
