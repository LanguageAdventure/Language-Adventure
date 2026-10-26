# Point-and-click channel outreach emails. Run from repo root: python3 img/email/build_pnc.py
import importlib.util, json
spec = importlib.util.spec_from_file_location('b', 'img/email/build_outreach.py'); b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
STEAM = 'https://store.steampowered.com/app/2204770/Language_Adventure/'
blue = lambda h, x: f'<a href="{h}" target="_blank"><b><font color="#0000ff">{x}</font></b></a>'
S, I = blue(STEAM, 'Steam'), blue(b.ITCH, 'itch.io')
P = {
 'en': dict(subject='Language Adventure – A stop-motion point-and-click adventure',
  p2="I'm Chris a solo developer from the UK and I've been making Language Adventure. It's a hand-made point-and-click adventure for learning English. It has subtitles in Spanish, Portuguese, French, German and Italian.",
  p3="An alien called Lingo has crash-landed in your garden and can't speak English yet. Explore a handmade town that's all filmed in stop motion, solve puzzles and help Lingo get home. Click on anything to hear what it is, and something funny about it, narrated by British comedian Adam Buxton.",
  p5a=f"A free demo is coming to {S} and {I} for Windows, Mac &amp; Linux on 13th January, but you can play it early by joining the play test through the form on the website.",
  p5b="Sign-ups are open from now until 26th November. You don't have to actually play test the game, so feel free to join even if you're just curious!",
  p6="I think it could be a fun one for your channel, and I'd love it if you'd give it a try. If you'd like to know anything, feel free to ask."),
 'fr': dict(subject='Language Adventure – un point-and-click en stop motion',
  p2="Je m'appelle Chris, développeur solo au Royaume-Uni, et je crée Language Adventure. C'est un jeu d'aventure point-and-click fait à la main pour apprendre l'anglais. Il a des sous-titres en espagnol, portugais, français, allemand et italien.",
  p3="Un extraterrestre appelé Lingo s'est écrasé dans ton jardin et ne parle pas encore anglais. Explore une ville faite à la main, entièrement filmée en stop motion, résous des énigmes et aide Lingo à rentrer chez lui. Clique sur n'importe quoi pour entendre ce que c'est, avec un petit commentaire drôle, raconté par l'humoriste britannique Adam Buxton.",
  p5a=f"Une démo gratuite sortira sur {S} et {I} pour Windows, Mac et Linux le 13 janvier, mais tu peux y jouer en avant-première en t'inscrivant au playtest via le formulaire sur le site.",
  p6="Je pense que ça pourrait plaire à ta chaîne, et j'aimerais beaucoup que tu l'essaies. Si tu veux savoir quoi que ce soit, n'hésite pas à demander."),
 'de': dict(subject='Language Adventure – ein Point-and-Click-Adventure in Stop-Motion',
  p2="Ich bin Chris, Solo-Entwickler aus Großbritannien, und entwickle gerade Language Adventure. Es ist ein handgemachtes Point-and-Click-Adventure zum Englischlernen. Es hat Untertitel auf Spanisch, Portugiesisch, Französisch, Deutsch und Italienisch.",
  p3="Ein Alien namens Lingo ist in deinem Garten notgelandet und kann noch kein Englisch. Erkunde eine handgemachte Stadt, die komplett in Stop-Motion gefilmt ist, löse Rätsel und hilf Lingo, nach Hause zu kommen. Klick auf irgendetwas, um zu hören, was es ist – mit einem lustigen Kommentar, erzählt vom britischen Komiker Adam Buxton.",
  p5a=f"Am 13. Januar erscheint eine kostenlose Demo auf {S} und {I} für Windows, Mac und Linux, aber du kannst sie schon vorher spielen, wenn du dich über das Formular auf der Website für den Playtest anmeldest.",
  p6="Ich glaube, es könnte gut zu deinem Kanal passen, und ich würde mich sehr freuen, wenn du es ausprobierst. Wenn du etwas wissen möchtest, frag gern."),
 'es': dict(subject='Language Adventure – una aventura point-and-click en stop motion',
  p2="Soy Chris, desarrollador en solitario de Reino Unido, y estoy creando Language Adventure. Es una aventura point-and-click hecha a mano para aprender inglés. Tiene subtítulos en español, portugués, francés, alemán e italiano.",
  p3="Un alienígena llamado Lingo se ha estrellado en tu jardín y todavía no habla inglés. Explora un pueblo hecho a mano y filmado por completo en stop motion, resuelve puzles y ayuda a Lingo a volver a casa. Haz clic en cualquier cosa para oír qué es, y algo gracioso sobre ello, con la narración del cómico británico Adam Buxton.",
  p5a=f"El 13 de enero saldrá una demo gratuita en {S} e {I} para Windows, Mac y Linux, pero puedes jugarla antes apuntándote al playtest con el formulario de la web.",
  p6="Creo que podría encajar muy bien en tu canal y me encantaría que lo probaras. Si quieres saber algo, no dudes en preguntar."),
 'it': dict(subject="Language Adventure – un'avventura punta e clicca in stop motion",
  p2="Sono Chris, sviluppo giochi da solo nel Regno Unito, e sto realizzando Language Adventure. È un'avventura punta e clicca fatta a mano per imparare l'inglese. Ha i sottotitoli in spagnolo, portoghese, francese, tedesco e italiano.",
  p3="Un alieno di nome Lingo si è schiantato nel tuo giardino e non parla ancora inglese. Esplora una città fatta a mano e girata interamente in stop motion, risolvi enigmi e aiuta Lingo a tornare a casa. Clicca su qualsiasi cosa per sentire cos'è, con un commento divertente, con la voce narrante del comico britannico Adam Buxton.",
  p5a=f"Il 13 gennaio uscirà una demo gratuita su {S} e {I} per Windows, Mac e Linux, ma puoi giocarci in anteprima iscrivendoti al playtest tramite il modulo sul sito.",
  p6="Penso che potrebbe piacere molto al tuo canale e mi farebbe davvero piacere se lo provassi. Se vuoi sapere qualcosa, chiedi pure."),
 'pt': dict(subject='Language Adventure – uma aventura point-and-click em stop motion',
  p2="Sou o Chris, um programador a solo do Reino Unido, e tenho estado a criar o Language Adventure. É uma aventura point-and-click feita à mão para aprender inglês. Tem legendas em espanhol, português, francês, alemão e italiano.",
  p3="Um extraterrestre chamado Lingo despenhou-se no teu jardim e ainda não fala inglês. Explora uma cidade feita à mão e filmada inteiramente em stop motion, resolve enigmas e ajuda o Lingo a voltar para casa. Clica em qualquer coisa para ouvires o que é, e algo engraçado sobre isso, com narração do comediante britânico Adam Buxton.",
  p5a=f"A 13 de janeiro vai sair uma demo gratuita no {S} e no {I} para Windows, Mac e Linux, mas podes jogá-la mais cedo inscrevendo-te no playtest através do formulário do site.",
  p6="Acho que pode ser uma boa escolha para o teu canal e adorava que o experimentasses. Se quiseres saber alguma coisa, não hesites em perguntar."),
}
TAG = {'en': 'EN', 'fr': 'FR', 'de': 'DE', 'es': 'ES', 'it': 'IT', 'pt': 'PT'}
subjects = {}
for lang, over in P.items():
    t = dict(b.T[lang]); t.update(over)
    t['p5a'] = t['p5a'].replace('{', '{{').replace('}', '}}')
    open(f'img/email/outreach-pnc-{lang}.html', 'w', encoding='utf-8').write(b.build(t))
    subjects[lang] = f"({TAG[lang]} Point & Click Outreach) {t['subject']}"
json.dump(subjects, open('img/email/subjects-pnc.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(subjects)
