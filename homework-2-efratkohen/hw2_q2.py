from enum import Enum
from collections import namedtuple


Type = Enum("Type", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def agent1_change_agent2 (other):
    other_list=list(other)
    l=len(other_list)
    if len(other_list)<=1:
        return other_list
    else:
        change=[]
        i=0
        if l%2==0:
            stop=l-2
        else:
            stop=l-3
            change.append(other_list[l-1])
        while i<=stop:
            if other_list[i].category.name=="SICK":
                if other_list[i+1].category.name=="SICK":
                    change.append(Agent(other_list[i].name, category=Type.DYING))
                    change.append(Agent(other_list[i+1].name, category=Type.DYING))
                if other_list[i+1].category.name=="DYING":
                    change.append(Agent(other_list[i].name, category=Type.DYING))
                    change.append(Agent(other_list[i+1].name, category=Type.DEAD))
                if other_list[i+1].category.name=="CURE":
                    change.append(Agent(other_list[i].name, category=Type.HEALTHY))
                    change.append(Agent(other_list[i+1].name, category=Type.CURE))
            if other_list[i].category.name=="DYING":
                if other_list[i+1].category.name=="SICK":
                    change.append(Agent(other_list[i].name,category=Type.DEAD))
                    change.append(Agent(other_list[i+1].name,category=Type.DEAD))
                if other_list[i+1].category.name=="DYING":
                    change.append(Agent(other_list[i].name, category=Type.DYING))
                    change.append(Agent(other_list[i+1].name,category=Type.DEAD))
                if other_list[i+1].category.name=="CURE":
                    change.append(Agent(other_list[i].name, category=Type.SICK))
                    change.append(Agent(other_list[i+1].name, category=Type.CURE))
            if other_list[i].category.name=="CURE":
                if other_list[i+1].category.name=="SICK":
                    change.append(Agent(other_list[i].name, category=Type.CURE))
                    change.append(Agent(other_list[i+1].name, category=Type.HEALTHY))
                if other_list[i+1].category.name=="DYING":
                    change.append(Agent(other_list[i].name, category=Type.CURE))
                    change.append(Agent(other_list[i+1].name, category=Type.SICK))
                if other_list[i+1].category.name=="CURE":
                    change.append(Agent(other_list[i].name, category=Type.CURE))
                    change.append(Agent(other_list[i+1].name, category=Type.CURE))
            i=i+2
        return change

def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Type.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    DATA=list(agent_listing)
    if len(DATA)<=1:
        return DATA
    else:
        healthy_dead=[]
        other=[]
        for condition in DATA:
            if (condition.category==Type.HEALTHY) or (condition.category==Type.DEAD):
                healthy_dead.append(condition)
            else:
                other.append(condition)
        if(len(other)==0):
            return healthy_dead
    other_change=agent1_change_agent2(other)
    result= other_change + healthy_dead 
    return result
