# Guide pour les Organisateurs

Bienvenue dans le guide de gestion du repository DevDay 2025! 👋

Ce document est destiné aux organisateurs et modérateurs du repository.

---

## 🎯 Responsabilités de l'Équipe d'Organisation

### 1. Validation des Pull Requests (24-48h)

**Checklist avant d'accepter une PR:**

- [ ] Speaker/Contributeur respecte le Code of Conduct
- [ ] Files sont dans le bon dossier
- [ ] Noms de fichiers sont clairs et professionnel
- [ ] Pas de contenu malveillant, illégal ou publicitaire
- [ ] Taille des fichiers respecte les limites
- [ ] Les liens fonctionnent et sont pertinents
- [ ] Pas de doublons avec contenu existant
- [ ] README est rempli correctement

**Rejet de PR:**
- Laisser un commentaire explicite
- Proposer des corrections
- Inviter à resoummettre
- Respecter le Code of Conduct

### 2. Modération du Contenu

**À surveiller:**

- 🚫 Contenu publicitaire sans permission
- 🚫 Spam ou contenu non pertinent
- 🚫 Violations de droits d'auteur
- 🚫 Contenu offensant ou harcelant
- 🚫 Liens malveillants

**Actions en cas de problème:**

1. Avertir le contributeur
2. Demander les modifications
3. Bloquer/Rejeter si nécessaire
4. Reporter les violations graves à contact@devday.be

### 3. Gestion des Issues

**Types d'Issues:**

| Type | Action | Délai |
|------|--------|-------|
| Bug | Enquêter, corriger | 24-48h |
| Feature | Évaluer, implémenter | Variable |
| Question | Répondre, documenter | 24h |
| Violationl | Alerter, enquêter | ASAP |

### 4. Maintenance du Repository

**Tâches régulières:**

- ✅ Vérifier les liens cassés
- ✅ Mettre à jour la documentation
- ✅ Corriger les typos
- ✅ Archiver les sessions complètes
- ✅ Publier les changements importants
- ✅ Répondre aux commentaires

---

## 📋 Processus de Validation des PRs

### Étape 1: Réception
```
PR soumise par un speaker
↓
Vérifier les informations de base
- Formulaire complété?
- Bonnes conventions de nommage?
- Fichiers acceptés?
```

### Étape 2: Review
```
Examiner le contenu
- Respect du Code of Conduct?
- Qualité du contenu?
- Pas de contenu propriétaire?
- Liens valides?
```

### Étape 3: Décision
```
✅ Accepter → Merge et remerciements
❌ Rejeter → Commentaires et suggestions
⏳ Attendre → Demander clarifications
```

### Étape 4: Publication
```
Merge la PR
↓
Vérifier la publication
↓
Remercier le contributeur
```

---

## 🔐 Sécurité & Modération

### Red Flags

Être attentif à:

- 🚩 Fichiers exécutables
- 🚩 Contenu "trop volumineux"
- 🚩 Liens suspects
- 🚩 Contenu dupliqué massif
- 🚩 Langage offensant
- 🚩 Spam de contributions

### Escalade des Violations

1. **Avertissement** - Message privé courtois
2. **Demande de correction** - Laisser une deadline
3. **Rejet** - Si non compliance
4. **Blocage** - Pour violations graves
5. **Exclusion** - Violateurs du Code of Conduct

### Escalade à contact@devday.be

Situations nécessitant escalade:
- Menaces ou harcèlement
- Contenu illégal
- Violations massives
- Doutes sur la sécurité

---

## 📊 Métriques à Suivre

### KPIs du Repository

Suivre et documenter:
- Nombre de sessions avec ressources
- Nombre de PRs reçues
- Temps moyen d'approbation
- Nombre d'issues
- Engagement de la communauté

**Rapport mensuel recommandé:**

```markdown
## Stats [Mois/Année]

- Sessions avec ressources: XX/41
- PRs reçues: XX
- PRs acceptées: XX
- Taux d'acceptation: XX%
- Temps moyen d'approval: Xh
- Issues résolues: XX
- Contributeurs uniques: XX
```

---

## 🚀 Tâches Before Event

### 2 Semaines Avant

- [ ] Vérifier que toutes les sessions ont des infos de base
- [ ] Envoyer rappels aux speakers pour qu'ils partagent
- [ ] Mettre à jour la documentation
- [ ] Tester tous les liens
- [ ] Préparer les communications

### 1 Semaine Avant

- [ ] Liste finale des sessions avec resources
- [ ] Vérifier la qualité du contenu
- [ ] Finaliser le README principal
- [ ] Préparer les remerciements
- [ ] Tester le repository sur mobile

### Jour de l'Événement

- [ ] Accès facile aux ressources pour les participants
- [ ] Support tech disponible
- [ ] Monitorer les issues
- [ ] Répondre rapidement aux questions

### Après l'Événement

- [ ] Archiver les sessions finalisées
- [ ] Documenter les learnings
- [ ] Préparer l'édition suivante
- [ ] Publier les statistiques finales
- [ ] Remercier les contributeurs

---

## 📞 Communication

### Canaux de Communication

| Canal | Usage | Urgence |
|-------|-------|---------|
| GitHub Issues | Questions techniques | Normal |
| GitHub PR Comments | Feedback sur contributions | Normal |
| Email (contact@devday.be) | Escalades graves | ASAP |
| Slack/Chat | Discussions rapides | Variable |
| Réunions équipe | Planification | Planning |

### Templates de Réponse

#### ✅ Acceptation PR

```markdown
Merci pour votre contribution! 🙏
Vos ressources pour la session [XX] ont été validées et mergées.
Vérifiez ici: [lien vers le fichier]
N'hésitez pas si vous avez besoin d'ajouter d'autres ressources.
```

#### ⏳ Demande de Clarification

```markdown
Merci pour la PR! 👍
Quelques questions avant validation:
- [Question 1]
- [Question 2]
Pouvez-vous clarifier cela? Merci!
```

#### ❌ Rejet

```markdown
Merci pour votre intérêt à contribuer.
Malheureusement, on ne peut pas accepter cette PR car:
- [Raison 1]
- [Raison 2]

Suggestions:
- [Solution 1]
- [Solution 2]

N'hésitez pas à resoummettre après modifications!
```

---

## 🔧 Maintenance Technique

### Vérifications Régulières

```bash
# Vérifier les fichiers de grande taille
find . -size +50M

# Vérifier les liens (si vous avez linkchecker)
linkchecker README.md

# Valider le markdown
mdl *.md

# Compter les contributions
git log --oneline | wc -l
```

### Backups

- Faire des backups réguliers
- Archiver les données importantes
- Documenter les migrations

---

## 📚 Documentation

### Mettre à Jour Régulièrement

- `README.md` - Vue d'ensemble
- `SESSIONS_INDEX.md` - Stats sessions
- `CHANGELOG.md` - Historique
- `FAQ.md` - Questions fréquentes
- `STRUCTURE.md` - Architecture

### Versioning

Utiliser [Semantic Versioning](https://semver.org/):
- `1.0.0` - Release première semaine
- `1.1.0` - Ajouts de features
- `1.0.1` - Bugfixes

---

## 🎓 Ressources pour Modérateurs

### Liens Utiles

- GitHub Docs: https://docs.github.com
- Code of Conduct: [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- Guide de contribution: [CONTRIBUTING.md](./CONTRIBUTING.md)
- Sessionize API: https://sessionize.com/api/v2/weqvopxi/view/All

### Training

- Lire les guides
- Participer aux PR reviews
- Apprendre des autres modérateurs
- Documenter les cas particuliers

---

## 🤝 Collaboration d'Équipe

### Réunions Recommandées

- **Weekly standup**: État des PRs, issues, métriques
- **Bi-weekly review**: Stratégie, modération, maintenance
- **Post-event debrief**: Learnings et améliorations

### Escalade Interne

```
PRs Bloquées → Demander review à [Person 2]
Modération Difficile → Consensus d'équipe
Décisions Importantes → Contact organization lead
```

---

## 📝 Checklist Final de Launch

- [ ] Code of Conduct en place et accepté
- [ ] Guide de contribution complété
- [ ] PR template configuré
- [ ] Issues templates créés
- [ ] 41 sessions avec dossiers
- [ ] Documentation complète
- [ ] Équipe modération formée
- [ ] Communication lancée
- [ ] Repository public
- [ ] Prêt pour contributions!

---

## 💡 Best Practices

1. ✅ Répondre vite aux PRs
2. ✅ Être respectueux et encourageant
3. ✅ Documenter les décisions
4. ✅ Partager la workload
5. ✅ Faire des retrospectives
6. ✅ Célébrer les contributions
7. ✅ Apprendre des erreurs
8. ✅ Éviter les burnouts

---

## Questions?

Contactez: contact@devday.be

**Merci pour votre implication dans DevDay 2025!** 🙌

