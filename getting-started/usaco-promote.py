import sys

sys.stdin = open("promote.in", "r")
sys.stdout = open("promote.out", "w")

bronze_before, bronze_after = map(int, input().split())
silver_before, silver_after = map(int, input().split())
gold_before, gold_after = map(int, input().split())
platinum_before, platinum_after = map(int, input().split())

gold_to_platinum_promotion = platinum_after - platinum_before
silver_to_gold_promotion = gold_after - gold_before + gold_to_platinum_promotion
bronze_to_silver_promotion = silver_after - silver_before + silver_to_gold_promotion

print(bronze_to_silver_promotion)
print(silver_to_gold_promotion)
print(gold_to_platinum_promotion)