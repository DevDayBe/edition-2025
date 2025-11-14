# Guide de Contribution

Merci de votre intérêt pour la contribution à DevDay 2025 ! 🎉

Ce guide vous aidera à soumettre vos ressources de manière efficace et conforme aux standards de la communauté.

---

## Code of Conduct

Ce projet respecte un Code of Conduct abaissé et inclusif. En participant, vous acceptez de respecter ses termes. Consultez [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) pour plus de détails.

**TL;DR: Soyez respectueux, bienveillant et professionnel.**

---

## Types de Contributions

### Speakers - Partagez vos ressources

Vous avez une session à DevDay 2025 ? Partagez vos :
- Slides (PDF, PPTX)
- Code samples et démos
- Articles et ressources
- Liens utiles et références

### Participants - Améliorez le repository

- Corrigez les erreurs (typos, liens cassés, etc.)
- Améliorez la documentation
- Suggérez de nouvelles structures
- Signalez des problèmes

### Organisateurs - Maintenez la qualité

- Révisez les Pull Requests
- Modérez le contenu
- Mettez à jour la documentation
- Assurez la conformité avec le Code of Conduct

---

## Processus de Contribution

### Pour les Speakers

#### 1. Fork & Clone
```bash
git clone https://github.com/DevDayBe/edition-2025.git
cd edition-2025
```

#### 2. Créer une branche
```bash
git checkout -b add/session-[numero]-[titre]
```

Format: `add/session-XX-titre-court` (remplacez les espaces par des tirets)

**Exemples:**
- `add/session-01-ia-equation-code`
- `add/session-25-testing-copilot`

#### 3. Ajouter vos ressources

1. Navigez vers le dossier de votre session:
   ```bash
   cd sessions/[numero]-[titre-session]/
   ```

2. Créez un `README.md` s'il n'existe pas:
   ```markdown
   # Session XX - [Titre]
   
   ## Speaker(s)
   - [Votre nom]
   
   ## Ressources
   - [Vos ressources ici]
   ```

3. Ajoutez vos fichiers (slides, code, etc.)

#### 4. Commit & Push

```bash
git add sessions/[numero]-[titre-session]/
git commit -m "docs: add session [XX] speaker resources

- Add slides for session [XX]
- Add demo code example
- Add reference links"
```

Utilisez le format:
- `docs: add` pour les ressources
- `docs: update` pour les modifications
- `fix: correct` pour les corrections

#### 5. Créer une Pull Request

1. Allez sur GitHub et créez une PR
2. Titre: `[Session XX] Add speaker resources for [Session Title]`
3. Description (template ci-dessous):

```markdown
## Session Info
- **Session Number**: XX
- **Session Title**: [Titre]
- **Speaker(s)**: [Vos noms]

## What's included
- [ ] Slides
- [ ] Code samples
- [ ] Demo files
- [ ] References/Articles
- [ ] Other: [Précisez]

## Additional notes
[Toute info additionnelle]

## Checklist
- [ ] J'ai lu et accepte le Code of Conduct
- [ ] J'ai vérifié les liens et fichiers
- [ ] La qualité du contenu est satisfaisante
- [ ] Les fichiers ne sont pas trop volumineux
```

#### 6. Attendre la révision

L'équipe d'organisation examinera votre PR et vous donnera un retour dans les **48 heures**.

---

### Pour les Autres Contributions

#### Corrections & Améliorations

1. Fork & clone le repository
2. Créer une branche: `fix/description-courte` ou `docs/amélioration`
3. Faites vos modifications
4. Commit avec un message clair
5. Créez une PR avec description

**Exemples de messages:**
- `fix: correct typo in session 05 readme`
- `docs: improve contributing guidelines`
- `feat: add new template for sessions`

---

## Standards de Qualité

### Fichiers & Formats

✅ **Acceptés:**
- PDF, PPTX, DOCX pour les slides/documents
- PNG, JPG, SVG pour les images
- ZIP, TAR.GZ pour les archives
- MD, TXT pour la documentation
- Code: .cs, .ts, .js, .py, .java, etc.

❌ **Non acceptés:**
- Fichiers exécutables (.exe, .bat, etc.)
- Contenu publicitaire sans modération
- Contenus piratés ou sous droits d'auteur violés
- Malware ou code malveillant

### Limites de Taille

- **Par fichier**: 50 MB maximum
- **Par PR**: 100 MB maximum
- **Par session**: ~200 MB recommandé

Si vous dépassez ces limites :
- Utilisez Git LFS pour les gros fichiers
- Divisez votre PR en plusieurs
- Compressez les archives

### Documentation

- Écrivez en **Markdown** (`.md`)
- Utilisez un français/anglais correct
- Ajoutez des descriptions claires
- Incluez des liens vers les ressources externes

---

## Guidelines de Contenu

### Slides & Présentation
- Résumé de 2-3 lignes du contenu
- Table des matières ou points clés
- Crédits et sources
- Liens vers ressources complètes si applicable

### Code & Démos
- `README.md` avec instructions pour exécuter
- Commentaires en anglais ou français
- License claire (MIT, CC, etc.)
- Dépendances listées

### Ressources & Articles
- Lien valide et actif
- Courte description (1-2 lignes)
- Auteur/source citée

### Speaker Info (optionnel)
```markdown
# Speaker Info

## [Nom du Speaker]
- **Affiliation**: [Entreprise/Titre]
- **LinkedIn**: [Lien]
- **Twitter/X**: [Handle]
- **Website**: [Lien]
- **Bio**: [Courte bio]
```

---

## Workflow de Révision

```
Submission → Automated Checks → Manual Review → Approved/Changes Requested → Merged
   (PR)         (CI/CD)          (Team)              (Feedback)           (Merged)
```

### Automated Checks
- ✓ Fichiers acceptés
- ✓ Pas de contenu malveillant
- ✓ Taille limite respectée
- ✓ Pas de conflits

### Manual Review (24-48h)
- ✓ Code of Conduct respecté
- ✓ Qualité du contenu
- ✓ Format et structure
- ✓ Commentaires constructifs

---

## Besoin d'Aide ?

### Questions Générales
📧 Contactez: contact@devday.be

### Questions Techniques (Git, GitHub, etc.)
- Consultez la [documentation GitHub](https://docs.github.com)
- Ouvrez une issue avec tag `question`
- Posez sur les discussions GitHub

### Problems avec une PR
- Commentez sur votre PR
- Mentionnez l'équipe (@DevDayBe/organizers)
- Demandez de l'aide directement

---

## Tips & Bonnes Pratiques

### Pour les Speakers ⭐

1. **Publier tôt**: Dès que possible après votre présentation
2. **Être complet**: Incluez tout ce que vous avez montré
3. **Documenter**: Ajoutez des explications et contexte
4. **Partager les sources**: Liens vers projets GitHub, articles, etc.
5. **Mettre à jour**: Corriger les typos ou ajouter des précisions
6. **Engager**: Répondez aux questions dans les issues

### Exemples d'Excellentes Sessions

Consultez des sessions bien documentées pour des exemples:
- `sessions/01-ia-devs-nouvelle-equation-code/` 
- `sessions/15-blazor-net10/`

---

## License

Par défaut, tous les contenus sont sous **Creative Commons Attribution 4.0 International (CC BY 4.0)**, sauf indication contraire du speaker.

```markdown
<!-- Ajouter en fin de votre README si différent: -->
## License
[Spécifiez votre license]
© 2025 [Votre nom]
```

---

## FAQ

**Q: Puis-je modifier ma contribution après?**  
A: Oui! Pushez simplement des commits supplémentaires sur la même branche.

**Q: Combien de temps avant que ma PR soit mergée?**  
A: 24-48 heures en moyenne pendant l'événement.

**Q: Puis-je faire plusieurs sessions?**  
A: Bien sûr! Créez une branche par session.

**Q: Et si je n'utilise pas Git?**  
A: Écrivez à contact@devday.be pour des options alternatives.

**Q: Puis-je partager du contenu vidéo?**  
A: Oui, mais hébergé externement (YouTube, Vimeo) avec lien.

---

## Merci! 🙏

Votre contribution rend DevDay 2025 plus riche et plus accessible. Merci de partager votre expertise avec la communauté!

**Happy contributing!** 🚀

