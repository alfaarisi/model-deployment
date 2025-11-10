# model-deployment

# NEWS CATEGORY CLASSIFIER

## Project Overview

A machine learning model that classifies news articles into 5 categories: Politics, Sports, Entertainment, Business, and Technology.

## The Journey: From 90% to Reality

### Initial Results

- **Training accuracy:** 90%
- **Expectation:** Production-ready classifier
- **Reality:** Significant performance gap on real-world data

### Real-World Testing

I tested the model on 25 fresh news articles from October 30, 2024, collected across all 5 categories.

**Results:**

- ✅ **8 articles (32%)** - Completely correct predictions
- 🟡 **9 articles (36%)** - Predicted valid alternative categories
- ❌ **8 articles (32%)** - Incorrect predictions

**Real-world accuracy: 32-68%** depending on how strictly you count ambiguous cases

**Best performing category:** Business (80% accuracy)

## Key Discovery: The Overfitting Problem

The 90% accuracy was misleading because:

1. **Test set too similar to training data** - Model memorized patterns instead of learning generalizable features
2. **Limited training data diversity** - Didn't represent real-world variation in writing styles and sources
3. **Simple train/test split** - Should have used cross-validation for more reliable metrics

**Critical lesson:** Test set accuracy ≠ real-world performance

## The Category Overlap Problem

After analyzing the results, I discovered news categories aren't mutually exclusive:

### Common Confusions (and why they make sense):

**1. Sports ↔ Entertainment** (Most frequent)

- Athletes are celebrities
- Sports events are entertainment
- Example: Celebrity athlete personal life stories
- **These overlaps are legitimate** - even human editors disagree

**2. Sports ↔ Business** (Player earnings, contracts)

- "Detroit Lions sign Aidan Hutchinson to $180M contract"
- Is this Sports (player news) or Business (contract/earnings)?
- **Valid ambiguity** - salary discussions are inherently both

**3. Tech ↔ Business** (Company partnerships, products)

- "Nvidia partners with Eli Lilly for AI drug discovery"
- Tech innovation or business partnership?
- Model predicted: Business (defensible choice)
- **Another legitimate overlap** - tech companies doing business

**4. Politics ↔ Business** (Economic policy, regulations)

- Trade deals, interest rates, corporate regulations
- Hard to separate policy from economics

### The "People vs. Field" Problem

The 8 completely wrong predictions revealed a pattern:

- Model confused articles ABOUT people in a field with articles ABOUT the field itself
- "Athlete's Earnings" → Predicted: Business | Should be: Sports

**Root cause:** Training data focused on field-specific content, not human interest stories about people in those fields.

## What I Learned

### About Machine Learning:

1. **Overfitting is real and subtle** - High test accuracy can hide poor generalization
2. **Data quality > Model complexity** - More diverse training data would help more than a fancier algorithm
3. **Cross-validation is essential** - Single train/test split gives unreliable metrics
4. **Real-world testing is crucial** - Always test on completely fresh, unseen data

### About the Problem Domain:

1. **News categories overlap naturally** - The problem itself is ambiguous
2. **Context matters** - Same keywords mean different things in different contexts
3. **Multi-label might be better** - Articles often legitimately belong to multiple categories
4. **Human interest is its own category** - Should have included this from the start

## Possible Improvements

1. **Collect more diverse training data**
    - Minimum 200-300 articles per category
    - Multiple news sources with different writing styles
    - Include various article lengths (headlines to full stories)
2. **Balance the dataset**
    - Ensure equal representation across categories
    - Address class imbalance issues
3. **Use cross-validation**
4. **Add n-grams to capture phrases**

## Technical Stack

- **Framework:** Flask
- **ML Library:** Scikit-learn
- **Vectorization:** CountVectorizer / TF-IDF
- **Model:**  Naive Bayes
- **Deployment:** GitHub Codespaces

## Conclusion

This project taught me that **building a model is just the beginning**. The real learning comes from:

- Rigorous real-world testing
- Understanding why models fail
- Analyzing error patterns
- Designing solutions that acknowledge limitations

Live Demo

https://model-deployment-54ik.onrender.com/

