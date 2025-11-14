# Session 22 - The art of data retention in PostgreSQL

## Speaker

- [**Stefan Fercot**](https://www.linkedin.com/in/stefan-fercot/)
  - [Data Egret](https://dataegret.com/)

## Session Info

- **Time**: 13:30 - 14:15 (45 min)
- **Type**: Session
- **Language**: English
- **Track**: Data, PostgreSQL, Performance
- **Level**: Intermediate

## Description

This session focuses on understanding and controlling data growth in PostgreSQL to maintain performance and simplify long-term maintenance. In the spirit of the *Bushido* code, it emphasizes discipline and foresight when managing large and evolving datasets.

The talk presents practical techniques to keep PostgreSQL databases lean and efficient. It covers how declarative partitioning simplifies table management and speeds up queries, how native LZ4 compression reduces storage overhead on oversized attributes, and how to archive or externalize outdated information using Foreign Data Wrappers. The session also demonstrates how to implement automated retention policies that manage data lifecycles with minimal developer effort.

This session is designed for developers and engineers who want to scale responsibly, maintain consistent performance, and apply thoughtful craftsmanship to the long-term health of their PostgreSQL systems.

## 📚 Resources

### Slides & Feedback

- Slides: [The Art of Data Retention in PostgreSQL](https://pgstef.github.io/talks/en/20251113_DevDayBE_the-art-of-data-retention-in-PostgreSQL.pdf)
- Feedback: https://openfeedback.io/devday2025/2025-11-13/969123

### References & Articles

- PostgreSQL documentation on table partitioning: https://www.postgresql.org/docs/current/ddl-partitioning.html
- Adyen blog post: [Efficiently Repartitioning Large Tables in PostgreSQL](https://www.adyen.com/knowledge-hub/efficiently-repartitioning-large-tables-in-postgresql)

## 📝 Notes

Data retention is not about deleting as much as possible, but about preserving what truly matters.
Keep what is essential, move less active data to more appropriate storage, archive historical data outside the main database, and drop what no longer has value.
This simple workflow keeps PostgreSQL tidy, maintainable, and focused on the data that really counts.

---

**Questions or suggestions?** Open a [GitHub Issue](https://github.com/DevDayBe/edition-2025/issues) or [contact the speaker](mailto:stefan.fercot@dataegret.com) directly.
