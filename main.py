# python3
def parallel_processing(num_threads, num_jobs, job_times):
    thread_schedule = [(0, i) for i in range(num_threads)]
    job_schedule = []
    for job_time in job_times:
        finish_time, thread_index = min(thread_schedule)
        job_schedule.append((thread_index, finish_time))
        thread_schedule[thread_index] = (finish_time + job_time, thread_index)
    return job_schedule

def main():
    num_threads, num_jobs = map(int, input().split())
    job_times = list(map(int, input().split()))
    job_schedule = parallel_processing(num_threads, num_jobs, job_times)
    for i in range(num_jobs):
        print(job_schedule[i][0], job_schedule[i][1])

if __name__ == "__main__":
    main()
