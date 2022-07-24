package bono.basiccrud.repository;

import bono.basiccrud.domain.Member;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.*;

class MemoryMemberRepositoryTest {
    MemoryMemberRepository repository = new MemoryMemberRepository();
    @AfterEach
    public void afterEach(){
        // 각 test간의 의존성이 없어야한다.
        repository.clearStore();
    }

    @Test
    public void save(){
        Member member = new Member();
        member.setName("bono");

        repository.save(member);
        Member result = repository.findById(member.getId()).get();
        System.out.println("result = " + (result == member));
        // Junit.jupiter.api
        //Assertions.assertEquals(member, result);
        // Assertj.core.api
        assertThat(member).isEqualTo(result);

    }
    @Test
    public void findByName(){
        Member member01 = new Member();
        member01.setName("bono");
        repository.save(member01);

        Member member02 = new Member();
        member02.setName("dono");
        repository.save(member02);

        Member result01 = repository.findByName("bono").get();
        assertThat(result01).isEqualTo(member01);
        assertThat(result01).isNotEqualTo(member02);
        Member result02 = repository.findByName("dono").get();
    }

    @Test
    public void findAll(){
        Member member01 = new Member();
        member01.setName("bono");
        repository.save(member01);

        Member member02 = new Member();
        member02.setName("dono");
        repository.save(member02);

        List<Member> results = repository.findAll();
        assertThat(results.size()).isEqualTo(2);
    }
}
