class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits_dict = defaultdict(int)

        for d in cpdomains:
            visits,domain = d.split(" ")
            visits = int(visits)
            visits_dict[domain] += visits
            for l in range(len(domain) - 1, - 1, - 1):
                if domain[l] == ".":
                    visits_dict[domain[l+1:]] += visits

        solution = []

        for k in visits_dict:
            solution.append(f"{visits_dict[k]} {k}")

        return solution

# The first 2 solutions are all similar. I solved this problem three time.