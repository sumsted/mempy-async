import asyncio
import aiohttp
import types
from resourcehelper import ResourceHelper


async def get_jobs(zip):
    response = await aiohttp.request('GET', 'https://data.usajobs.gov/api/jobs?LocationId=' + zip)
    result = await response.read_and_close(decode=True)
    total_jobs = int(result['TotalJobs'])
    return total_jobs


async def async_jobs(zips):
    total = 0
    coroutines = [get_jobs(zip) for zip in zips]
    for result in asyncio.as_completed(coroutines):
        total += await result
    return total


if __name__ == '__main__':
    rh = ResourceHelper(__file__)
    
    zips = ['79936', '90011', '60629', '90650', '90201', '77084', '92335', '78521', '77449', '78572',
            '90250', '90280', '11226', '90805', '91331', '08701', '90044', '92336', '00926', '94565',
            '10467', '92683', '75052', '91342', '92704', '30044', '10025', '92503', '92804', '78577',
            '75217', '92376', '93307', '10456', '10002', '91911', '91744', '75070', '77036', '93722',
            '92345', '60618', '93033', '93550', '95076', '11230', '11368', '37013', '11373', '79912',
            '37211', '30043', '11206', '10453', '92154', '11355', '95823', '77479', '91706', '10458',
            '92553', '90706', '23464', '11212', '60617', '91709', '11214', '11219', '91910', '22193',
            '77429', '93535', '66062', '93257', '30349', '60647', '77584', '10452', '77573', '11377',
            '11207', '77494', '75211', '11234', '28269', '11235', '94544', '10029', '60625', '89110',
            '92509', '77083', '91335', '85364', '87121', '10468', '90255', '93065', '91710', '10462']

    loop = asyncio.get_event_loop()
    jobs = loop.run_until_complete(async_jobs(zips))
    print('\njobs available: %s' % jobs)
    
    rh.usage()